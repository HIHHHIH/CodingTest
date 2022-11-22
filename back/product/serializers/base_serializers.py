from rest_framework import serializers
from .serializers import *
from ..models import *

class PostProblemSerializer(serializers.ModelSerializer):
        testcases = TestCaseSerializer(many=True, read_only = True, source="opened_testcase")
        class Meta:
            model = problem
            fields = ('testcases', 'codes', 'problem_id','lecture' ,'assignment','title','description','restriction', 'timelimit','memorylimit')
