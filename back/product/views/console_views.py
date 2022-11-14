from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers.serializers import *
from ..module.code_runner import *
from ..module.pylama_runner import *
from ..module.case_tester import *
"""
1. run_code
url: 127.0.0.1:8000/study/run
위 url 접속해서 아래 {}내용 복붙해서 POST하면 작성한 코드가 아래 입력에 어떻게 반응하는지 볼 수 있음.

{
"problem":1,
"user":1,
"user_code":"this is the written code"
}


2. grade_code
url: 127.0.0.1:8000/study/grade
확인방법은 run_code와 동일

"""
example = '''
def solution(n):
    _curr, _next =0, 1
    for _ in range(n)
        _curr, _next = _next, _curr + _next
        return _curr
    result = solution(3)
    print(result)
'''


@api_view(['POST'])
def submit_code(request):  # 코드 제출
    """
    :param request: ['user_id', 'problem_id, 'user_code]
    :return:
    """

    user_id = request.data['user_id']
    problem_id = request.data['problem_id']
    user_code = request.data['user_code']  # 유저가 작성한 코드

    sessions = session.objects.filter(user=user_id, problem=problem_id)
    for item in sessions:
        pk = item.pk
    current_session = session.objects.get(pk=pk)

    if current_session.submission_count != 0:  # 코드 제출 횟수 3번으로 제한. 최초값 3에서 1씩 차감.
        current_session.submission_count -= 1
        current_session.save()
        # print(current_session.submission_count)

        # 테스트 케이스 채점
        user_code = request.data['user_code']
        problem_id = request.data['problem']
        testcases = testcase.objects.filter(problem=problem_id)

        inputs = None  #모든 테스트 케이스 인풋 리스트
        outputs = None  #모든 테스트 케이스 아웃풋 리스트
        testcase_result = run_test(user_code, inputs, outputs)  # 테스트 케이스 실행 결과

        # 가독성 검사 : pylama
        pylama_output = pylama_run(user_code)
        # pylama_output = {"mypy": [20, msg1, msg2, ...],"pylint": [20, msg1, msg2, ...],"eradicate": [20, msg1, msg2, ...],"radon": [20, msg1, msg2, ...],"pycodestyle": [20, msg1, msg2, ...]}

        pylama_output = {}
        '''
        
        multimetric
        
        '''
        multimetric_output = {}

        '''
        
        openAIcodex
        
        '''
        openAIcodex_output = {}

        output = None  # 코드 채점 결과, dictionary
        return Response([testcase_result, pylama_output, multimetric_output, openAIcodex_output])  # 프론트에 코드 채점 결과 전달
    else:
        Response({"result": "you can't submit more than 3 times."})


@api_view(['POST'])
def run_code(request):  # 코드 실행
    user_code = request.data['user_code']  # user가 작성한 코드
    line_number, message = execute(user_code)
    return Response({"line_number": line_number, "message": message})  # 프론트에 코드 실행 결과 전달


@api_view(['POST'])
def grade_code(request):  # 코드 채점

    """

    :param request: [user_code, problem_id]
    :return:
    """

    user_code = request.data['user_code']
    problem_id = request.data['problem']
    testcases = testcase.objects.filter(problem=problem_id)
    result = []  # 테스트 케이스 실행 결과
    for case in testcases:
        result.append(run_test(user_code, case.input, case.output))

    return Response({"result": result})  #임시 아웃풋
