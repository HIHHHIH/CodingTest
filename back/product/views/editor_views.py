from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers.serializers import *
from django.http import HttpResponse, JsonResponse
import json


@api_view(['POST'])
def save_code(request):
    serializer = CodeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"error": "serializer is not valid"})


@api_view(['POST'])
def download_code(request):
    serializer = CodeSerializer(data=request.data)
    if serializer.is_valid():
        with open("my code.txt", "w") as f:
            f.write(json.dumps(serializer.data))
        return Response(serializer.data)
    else:
        return Response({"error": "serializer is not valid"})