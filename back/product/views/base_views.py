# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import *
from ..serializers.serializers import *
from ..serializers.base_serializers import *
from ..module.case_tester import run_specific_test, rand_name
import json
# Create your views here.


@api_view(['GET'])
def helloAPI(request):
    return HttpResponse("hello world!")


@api_view(['GET'])
def get_recent(request, user_id):

    problem_id = request.session.get(user_id)  #세션에서 문제 가져오기

    if problem_id is None:
        problems = problem.objects.filter(problem_id=0)
        testcases = testcase.objects.filter(problem_id=0)
        current_code = code.objects.filter(user_id=user_id).filter(problem_id=0)
    else:
        problems = problem.objects.filter(problem_id=problem_id)
        testcases = testcase.objects.filter(problem_id=problem_id)
        current_code = code.objects.filter(user_id=user_id).filter(problem_id=problem_id)

    problem_serializer = ProblemSerializer(problems, many=True)
    test_serializer = TestCaseSerializer(testcases, many=True)
    code_serializer = CodeSerializer(current_code, many=True)

    return Response([problem_serializer.data, test_serializer.data, code_serializer.data])

@api_view(['POST'])
def get_lectures(request):
    items = lecture.objects.all()
    serializer = LectureSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def get_assignments(request):
    try:
        lecture_id = request.data["lecture_id"]
        items = assignment.objects.select_related('lecture').filter(lecture_id=lecture_id)
        serializer = AssignmentSerializer(items, many=True)
        return Response(serializer.data)

    except Exception as e:
        print(e)
        return JsonResponse({"result":"the json is not correctly serialized"})


@api_view(['POST'])
def get_problem(request):
    try:
        lecture_id = request.data["lecture_id"]
        assignment_id= request.data["assignment_id"]
        items = (problem.objects
                        .select_related('assignment')
                        .filter(lecture=lecture_id, assignment= assignment_id )
                    )
        serializer = ProblemSerializer(items, many=True)
        return Response(serializer.data)

    except Exception as e:
        print(e)
        return JsonResponse({"result":"the json is not correctly serialized"})


@api_view(['GET'])
def get_main_page(request, problem_id, user_id):
    current_problem = problem.objects.filter(problem_id= problem_id )
    problem_serializer = ProblemSerializer(current_problem, many=True)

    request.session[user_id] = problem_id  #세션에 지금 접속한 user_id의 problem_id 저장

    testcases = testcase.objects.filter(problem_id=problem_id)
    test_serializer = TestCaseSerializer(testcases, many=True)

    current_code = code.objects.filter(user_id=user_id).filter(problem_id=problem_id)
    code_serializer = CodeSerializer(current_code, many=True)

    current_session = session.objects.filter(user_id=user_id, problem_id = problem_id)
    if not current_session.exists():  #problem을 처음 열람할 시 session 생성
        current_user = user.objects.get(user_id = user_id)
        cp = problem.objects.get(problem_id = problem_id)  # problem
        session.objects.create(submission_count = 3, problem = cp, user = current_user)

    return Response([problem_serializer.data, test_serializer.data, code_serializer.data])


@csrf_exempt
@api_view(['POST'])
def info_problem(request):
    try:
        lecture_id = request.data["lecture_id"]
        assignment_id= request.data["assignment_id"]
        problem_id = request.data["problem_id"]

        item = (problem.objects
                        .select_related('assignment', 'lecture')
                        .get( lecture= lecture_id, assignment= assignment_id, problem_id= problem_id)
                    )
        serializer = PostProblemSerializer(item, many=False)
        return Response(serializer.data)

    except Exception as e:
        print(e)
        return JsonResponse({"result":"the json is not correctly serialized"})


@api_view(['POST'])
def load_code(request):
    try:
        problem_id = request.data["problem_id"]
        student_id = request.data["student_id"]

        item = (code.objects
                    .filter( user= student_id, problem= problem_id).order_by('-modified_date')
                    )
        serializer = CodeSerializer(item , many=True)

        if(serializer.data):
            return Response(serializer.data[0])
        else:
            return Response(serializer.data)

    except Exception as e:
        print(e)
        return JsonResponse({"result":"the json is not correctly serialized"})


"""
1. run_specific_testcase
url: 127.0.0.1:8000/study/testcase/
특정 test case 실행

{
"input" : "1 2"
"output" : "3"
"user_code":"this is the written code"
}

"""

@api_view(['POST'])
def run_specific_testcase(request):
    try:
        input = request.data["input"]
        output = request.data["output"]
        user_code = request.data["user_code"]

        input_list = []
        output_list = []
        if(len(input.split(" ")) != 1) :
            input_list.append(list(map(int, input.split(" "))))  # string을 int로 변환
        else :
            input_list.append(int(input))

        if(len(output.split(" ")) != 1) :
            output_list.append(list(map(int, output.split(" "))))
        else :
            output_list.append(int(output))


        # user_code = "def solution(a,b,c):\n\treturn a+b+c"  #실행예시
        # input = [[1,2,3]]  # 모든 테스트 케이스 인풋 리스트
        # output = [6]  # 모든 테스트 케이스 아웃풋 리스트
        testcase_result, user_output = run_specific_test(user_code, input_list, output_list, rand_name())

        return Response({'result' : testcase_result[0], 'output' : user_output[0]})
    except Exception as e:
        return Response({'result' : "F", 'output' : "Unknown Error"})
