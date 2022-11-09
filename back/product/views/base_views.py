# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import *
from ..serializers.serializers import *
import json
# Create your views here.


@api_view(['GET'])
def helloAPI(request):
    return HttpResponse("hello world!")


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
        return JsonResponse({"result":"the json is not correctly serialized"})


@api_view(['GET'])
def get_main_page(request, problem_id, user_id):
    current_problem = problem.objects.select_related('assignment').filter(problem_id= problem_id )
    problem_serializer = ProblemSerializer(current_problem, many=True)

    testcases = testcase.objects.filter(problem_id=problem_id)
    test_serializer = TestCaseSerializer(testcases, many=True)

    current_code = code.objects.filter(user_id=user_id).filter(problem_id=problem_id)
    code_serializer = CodeSerializer(current_code, many=True)

    current_session = None

    current_session = session.objects.filter(user_id=user_id, problem_id = problem_id)

    if not current_session.exists(): ## problem을 처음 열람할 시 session 생성
        current_user = user.objects.get(user_id = user_id) 
        cp = problem.objects.get(problem_id = problem_id) ## problem
        session.objects.create(submission_count = 3, problem = cp, user = current_user) ## 문제점: create가 반환하는 type은 serializer에 넣을 수 없다.
    
    current_session = session.objects.filter(user_id=user_id, problem_id = problem_id) ## 문제점: 새로 생성하고 다시 select해야한다.
    session_serializer = SessionSerializer(current_session, many=True)
        

    return Response([problem_serializer.data, test_serializer.data, code_serializer.data, session_serializer.data])


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

        serializer = ProblemSerializer(item, many=False)
        return Response(serializer.data)

    except Exception as e:
        return JsonResponse({"result":"the json is not correctly serialized"})
        # result = {
        #         "id" : problems.problem_id,
        #         "title": problems.title,
        #         "assignmentTitle" : problems.assignment.title,
        #         "lectureTitle": problems.lecture.title,
        #         "description": problems.description,
        #         "restriction": problems.restriction,
        #         "reference": problems.reference,
        #         "timelimit": problems.timelimit,
        #         "memorylimit": problems.memorylimit,
        #     }
        # return JsonResponse({'result' : result})





# @api_view(['GET'])
# def show_problem(request, lecture_id, assignment_id, problem_id ):
#     problems = (problem.objects
#                     .select_related('assignment', 'lecture')
#                     .get( lecture_id= lecture_id, assignment_id= assignment_id, problem_id= problem_id)
#                 )
#
#     result = {
#             "id" : problems.problem_id,
#             "title": problems.title,
#             "assignmentTitle" : problems.assignment.title,
#             "lectureTitle": problems.lecture.title,
#             "description": problems.description,
#             "restriction": problems.restriction,
#             "reference": problems.reference,
#             "timelimit": problems.timelimit,
#             "memorylimit": problems.memorylimit,
#         }
#
#     return JsonResponse({'result' : result})
