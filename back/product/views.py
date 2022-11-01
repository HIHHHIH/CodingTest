from django.shortcuts import render
from django.http import JsonResponse 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import ProblemSerializer
import random
# Create your views here.



# Create your views here.

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def randomProblems(request, id):
    totalProblems = Problem.objects.all()
    randomProblems = random.sample(list(totalProblems), id)
    serializer = ProblemSerializer(randomProblems, many=True) #many 부분을 통해 다량의 데이터도 직렬화 진행
    return Response(serializer.data)

@api_view(['GET'])
def specificProblems(request, id):
    spProblems = Problem.objects.get(problem_id = id)
    print(spProblems)
    serializer = ProblemSerializer(spProblems) #many 부분을 통해 다량의 데이터도 직렬화 진행
    return Response(serializer.data)

@api_view(['GET'])
def specificStudent(request, id):
    ongoings = (ongoing.objects
        .filter(student_id = id)
        .select_related('student', 'problem')
        .all())

    result = [{
            "id": ongoing.student.student_id,
            "name": ongoing.student.student_name,
            "problem_id": ongoing.problem.problem_id,
            "problem_name": ongoing.problem.problem_name,
            "description": ongoing.problem.description,
            "restriction": ongoing.problem.restriction,
            "test_case": ongoing.problem.test_case,
        } for ongoing in ongoings]
    
    print(result)
    return JsonResponse({'result' : result}) 