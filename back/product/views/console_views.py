from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers.serializers import *
from ..module.code_runner import *
from ..module.pylama_runner import *
from ..module.case_tester import *
from ..module.multimetric_runner import *
from ..module.code_explainer import *
from ..module.copydetect_runner import *

import re


def grade(user_code, testcases):
    inputs = testcases.values_list('input', flat=True)  # 모든 테스트 케이스 인풋
    input_list = []
    for input in inputs:
        temp_list = input.split(" ")
        int_input = list(map(int, temp_list))  # string을 int로 변환
        input_list.append(int_input)
    outputs = list(testcases.values_list('output', flat=True))
    output_list = list(map(int, outputs))

    testcase_result, user_output = run_test(user_code, input_list, output_list, rand_name())

    # 채점 점수
    score = sum(20 for value in testcase_result.values() if value == 'P')

    # 오픈 테스트 케이스
    open_case_sum = []
    for i in range(3):
        case_result = {'result': '통과' if testcase_result[i] == 'P' else '실패',
                       'input': f'solution({",".join(str(num) for num in input_list[i])})',
                       'correct_output': str(output_list[i]),
                       'your_output': str(user_output[i])}
        open_case_sum.append(case_result)

    # 히든 테스트 케이스
    hidden_case_sum = []
    for i in range(2, 5):
        case_result = {'result': '통과' if testcase_result[i] == 'P' else '실패'}
        hidden_case_sum.append(case_result)

    return score, open_case_sum, hidden_case_sum


@api_view(['POST'])
def submit_code(request):  # 코드 제출
    """
    :param request: ['problem_id', 'user_id', 'user_code', 'code_idx]
    """

    '''
           {
               "problem_id": 0,
               "user_id": 0,
               "user_code": "def solution(a,b):\n\td=a*b\n\treturn d",
               "code_idx": "2"
           }
   '''

    user_id = request.data['user_id']
    problem_id = request.data['problem_id']
    user_code = request.data['user_code']  # 유저가 작성한 코드
    solution_code = solution.objects.get(problem_id=problem_id).answer_code  # 정답 코드

    sessions = session.objects.filter(user=user_id, problem=problem_id)
    for item in sessions:
        pk = item.pk
    current_session = session.objects.get(pk=pk)

    #잔여 제출 횟수가 없다면 제출 못함.
    if current_session.submission_count == 0:
        return Response({"result": "you can't submit more than 3 times."})

    current_session.submission_count -= 1
    current_session.save()
    code_slot = 6 - current_session.submission_count
    # 제출한 코드 DB에 저장
    request.data["code_idx"] = code_slot
    serializer = CodeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    file_name = rand_name()+'.py'  #유저가 작성한 코드를 랜덤한 이름의 임시 파일로 저장함.
    with open(file_name, 'w') as f:
        f.write(user_code)
        f.close()


    # 테스트 케이스 채점
    testcases = testcase.objects.filter(problem=problem_id)
    score, open_case_sum, hidden_case_sum = grade(user_code, testcases)

    testcase_result = {"score": score,
                       "open_results": open_case_sum,
                       "hidden_results": hidden_case_sum
                       }

    # 효율성 검사 : multimetric
    user_halstead, user_loc, user_control_complexity, user_data_complexity = multimetric_run(user_code)
    sol_halstead, sol_loc, sol_control_complexity, sol_data_complexity = multimetric_run(solution_code)

    halstead_score = 25 if user_halstead < sol_halstead else (sol_halstead / user_halstead) * 25
    loc_score = 25 if user_loc < sol_loc else (sol_loc / user_loc) * 25
    control_complexity_score \
        = 25 if user_control_complexity < sol_control_complexity \
        else (sol_control_complexity / user_control_complexity) * 25
    data_complexity_score \
        = 25 if user_data_complexity < sol_data_complexity \
        else (sol_data_complexity / user_data_complexity) * 25

    multimetric_output = {"loc_score": loc_score,
                          "data_complexity_score": data_complexity_score,
                          "control_complexity_score": control_complexity_score,
                          "halstead_score": halstead_score}

    # 가독성 검사 : pylama
    pylama_output = pylama_run(file_name)
    """
    {"mypy": {"score": 점수, "msg": ["msg1", "msg2", ...]},
    "pylint": {"score": 점수, "msg": ["msg1", "msg2", ...]},
    "eradicate": {"score": 점수, "msg": ["msg1", "msg2", ...]},
    "radon": {"score": 점수, "msg": ["msg1", "msg2", ...]},
    "pycodestyle": {"score": 점수, "msg": ["msg1", "msg2", ...]}
    }
    """
    # 코드 설명 : openai
    openAIcodex_output = explain_code(user_code)

    # 표절 검사
    reference_codes = code.objects.filter(problem_id=problem_id)
    reference_codes_i = []
    for i in reference_codes:
        if(i.user.user_id != user_id and i.code_idx > 3):
            reference_codes_i.append(i.user_code)
    skeleton_code = problem.objects.get(problem_id=problem_id).skeleton
    plagiarism_detector = CopyDetect(user_id,problem_id,user_code,reference_codes_i,skeleton_code)
    plagiarism_detector.setup()
    plagiarism = plagiarism_detector.run_detector()
    plagiarism_detector.teardown()

    # 참고 링크
    reference_list = []
    references = reference.objects.filter(problem=problem_id)  #make iterable
    for item in references.values():
        ref = {}
        ref['title'] = item['title']
        ref['url'] = item['url']
        reference_list.append(ref)
    """
    [
    {
    'title': string,
    'url': string
    },
    {
    'title': string,
    'url': string
    },
    {
    'title': string,
    'url': string
    }
    """
    os.remove(file_name)  #임시 파일 삭제
    # 정상 메세지
    result = 'your code is successfully submitted'

    return Response( # 프론트에 코드 채점 결과 전달
        {'result': result, 'testcase_output':testcase_result, 'pylama_output':pylama_output,
         'multimetric_output': multimetric_output, 'plagiarism':plagiarism,
         'codex_output':openAIcodex_output, 'solution_code':solution_code, 'reference':reference_list})



@api_view(['POST'])
def run_code(request):  # 코드 실행
    user_code = request.data['user_code']  # user가 작성한 코드
    is_success, line_number, message = execute(user_code)
    return Response({"success": is_success, "line_number": line_number, "message": message})  # 프론트에 코드 실행 결과 전달


@api_view(['POST'])
def grade_code(request):  # 코드 채점

    """
       {
               "problem_id": 0,
               "user_code": "def solution(a,b):\n\td=a*b\n\treturn d"
       }
    """

    user_code = request.data['user_code']
    problem_id = request.data['problem_id']
    testcases = testcase.objects.filter(problem=problem_id).order_by('idx')

    score, open_case_sum, hidden_case_sum = grade(user_code, testcases)

    result = {"score": score,
              "open_results": open_case_sum,
              "hidden_results": hidden_case_sum
              }

    return Response(result)
