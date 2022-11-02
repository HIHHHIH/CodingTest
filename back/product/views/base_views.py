# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import *
import json
# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return HttpResponse("hello world!")

@api_view(['GET'])
def get_lectures(request):
    lectures = lecture.objects.all()

    result = [{
            "id": lecture.lecture_id,
            "title": lecture.title,
        } for lecture in lectures]

    return JsonResponse({'result' : result})

@api_view(['GET'])
def get_assignments(request, lecture_id):
    assignments = (assignment.objects
                    .select_related('lecture')
                    .filter( lecture = lecture_id  )
                    )

    result = [{
            "id" : assignment.assignment_id,
            "title": assignment.title,
            "deadline": assignment.deadline,
        } for assignment in assignments]

    return JsonResponse({'result' : result})

@api_view(['GET'])
def get_problem(request, lecture_id, assignment_id ):
    problems = (problem.objects
                    .select_related('assignment')
                    .filter(assignment_id= assignment_id )
                )

    result = [{
            "id" : problem.problem_id,
            "title": problem.title,
            "assignmentTitle" : problem.assignment.title,
            "lectureTitle": problem.lecture.title,
            "description": problem.description,
            "restriction": problem.restriction,
            "reference": problem.reference,
            "timelimit": problem.timelimit,
            "memorylimit": problem.memorylimit,
        } for problem in problems]

    return JsonResponse({'result' : result})

@csrf_exempt
def info_problem(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode())
            lecture_id = data['lecture_id']
            assignment_id = data['assignment_id']
            problem_id = data['problem_id']

            problems = (problem.objects
                            .select_related('assignment', 'lecture')
                            .get( lecture_id= lecture_id, assignment_id= assignment_id, problem_id= problem_id)
                        )



            result = {
                    "id" : problems.problem_id,
                    "title": problems.title,
                    "assignmentTitle" : problems.assignment.title,
                    "lectureTitle": problems.lecture.title,
                    "description": problems.description,
                    "restriction": problems.restriction,
                    "reference": problems.reference,
                    "timelimit": problems.timelimit,
                    "memorylimit": problems.memorylimit,
                }
            return JsonResponse({'result' : result})
        except Exception as e:
            print(e)
            return HttpResponse(404)

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
