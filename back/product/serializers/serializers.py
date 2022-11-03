from rest_framework import serializers
from ..models import *


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = problem
        fields = '__all__'


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = code
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = lecture
        fields = '__all__'


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = testcase
        fields = '__all__'


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = solution
        fields = '__all__'


class UserLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_lecture
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = assignment
        fields = '__all__'
