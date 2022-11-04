from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers.serializers import *

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



@api_view(['POST'])
def run_code(request):  #코드 실행
    serializer = CodeSerializer(data=request.data)
    if serializer.is_valid():
        user_code = serializer.data['user_code']  #user가 작성한 코드

        """
        user_code를 실행하는 코드 작성
        """

        output = None  #코드 실행 결과, string
        return Response({"result": output})  #프론트에 코드 실행 결과 전달
    else:
        return Response({"error":"serializer is not valid"})


@api_view(['POST'])
def grade_code(request):  #코드 실행
    serializer = CodeSerializer(data=request.data)
    if serializer.is_valid():
        user_code = serializer.data['user_code']  #user가 작성한 코드

        """
        user_code를 채점하는 코드 작성
        """

        output = None  # 코드 채점 결과, dictionary
        return Response(output)  #프론트에 코드 실행 결과 전달
    else:
        return Response({"error":"serializer is not valid"})
