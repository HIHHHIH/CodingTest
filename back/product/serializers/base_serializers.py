from rest_framework import serializers
from ..models import *


class PostProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = problem
        fields = '__all__'

class PostpostLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = lecture
        fields = '__all__'

class PostAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = assignment
        fields = '__all__'
