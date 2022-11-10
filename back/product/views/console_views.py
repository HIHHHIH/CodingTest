from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers.serializers import *
from ..module.code_runner import *

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
    user_code = request.data['user_code']  # user가 작성한 코드

    sessions = session.objects.filter(user=user_id, problem=problem_id)
    for item in sessions:
        pk = item.pk
    current_session = session.objects.get(pk=pk)

    if current_session.submission_count != 0: #코드 제출 횟수 3번으로 제한. 최초값 3에서 1씩 차감.
        current_session.submission_count -= 1
        current_session.save()
        """
        코드 제출해서 평가받는 코드 작성
        """
    else:
        Response({"result": "you can't submit more than 3 times."})

    #제출 회수 +1 하는 코드 작성해야함.
    output = None
    return Response({"result": current_session.submission_count})  # 프론트에 코드 실행 결과 전달


@api_view(['POST'])
def run_code(request):  # 코드 실행
    user_code = request.data['user_code']  # user가 작성한 코드
    output = execute(user_code)
    return Response({"result": output})  # 프론트에 코드 실행 결과 전달


@api_view(['POST'])
def grade_code(request):  #코드 채점
    serializer = CodeSerializer(data=request.data)
    if serializer.is_valid():
        user_code = serializer.data['user_code']  #user가 작성한 코드

        """
        user_code를 채점하는 코드 작성
        """
        # 가독성 검사 : pylama
        pylama_output = pylama_run(user_code)

        output = None  # 코드 채점 결과, dictionary
        return Response(output)  #프론트에 코드 실행 결과 전달
    else:
        return Response({"error":"serializer is not valid"})
