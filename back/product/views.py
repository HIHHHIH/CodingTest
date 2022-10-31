from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Problem
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
    serializer = ProblemsSerializer(randomProblems, many=True) #many 부분을 통해 다량의 데이터도 직렬화 진행
    return Response(serializer.data)
