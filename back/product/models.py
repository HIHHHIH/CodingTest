from django.db import models

# Create your models here.
class Problem(models.Model):
    problem_id = models.CharField(max_length=200)
    problem_name = models.TextField()
    description = models.TextField()
    restriction = models.TextField()
    test_case = models.IntegerField()

class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.TextField()

class ongoing(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem , on_delete=models.CASCADE)
