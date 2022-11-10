from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers.serializers import *
import json


@api_view(['POST'])
def save_code(request):
    """
    :param request: [problem_id, user_id, user_code, code_idx]
    :return:
    """

    problem_id = request.data['problem']
    user_id = request.data['user']
    user_code = request.data['user_code']
    code_idx = request.data['code_idx']

    saved_code = code.objects.filter(problem=problem_id).filter(user=user_id).filter(code_idx=code_idx)
    if saved_code.exists():
        saved_code.update(user_code=user_code)
        return Response({"result":"your code is successfully edited"})
    else:
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": "your code is successfully saved"})
        else:
            return Response({"result": "serializer is not valid"})


@api_view(['POST'])
def download_code(request):
    serializer = CodeSerializer(data=request.data)
    if serializer.is_valid():
        with open("my code.txt", "w") as f:
            f.write(json.dumps(serializer.data))
        return Response(serializer.data)
    else:
        return Response({"error": "serializer is not valid"})
