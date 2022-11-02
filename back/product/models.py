from django.db import models

# Create your models here.
class lecture(models.Model):
    lecture_id = models.IntegerField(primary_key=True)
    title = models.TextField()


class user(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.TextField( null = False )
    password = models.TextField( null = False )
    role = models.TextField()
    created_date = models.DateField()


class assignment(models.Model):
    assignment_id = models.IntegerField(primary_key=True)
    lecture = models.ForeignKey(lecture , on_delete=models.CASCADE)
    title = models.TextField()
    deadline = models.DateTimeField()


class problem(models.Model):
    problem_id = models.IntegerField(primary_key=True)
    lecture = models.ForeignKey(lecture , on_delete=models.CASCADE)
    assignment = models.ForeignKey(assignment , on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    restriction = models.TextField(null = True)
    reference = models.TextField(null = True)
    timelimit = models.IntegerField()
    memorylimit = models.IntegerField()


class testcase(models.Model):
    testcase_id = models.AutoField(primary_key=True)
    problem = models.ForeignKey(problem , on_delete=models.CASCADE)
    # show number of testcase in that problem
    idx = models.IntegerField()
    isHidden = models.BooleanField()
    input = models.TextField()
    output = models.TextField()


class solution(models.Model):
    solution_id = models.AutoField(primary_key=True)
    problem = models.ForeignKey(problem , on_delete=models.CASCADE)
    created_date = models.DateField()
    modified_date = models.DateField()
    answer_code = models.TextField()


class code(models.Model):
    code_id = models.AutoField(primary_key=True)
    problem = models.ForeignKey(problem , on_delete=models.CASCADE)
    user = models.ForeignKey(user , on_delete=models.CASCADE)
    created_date = models.DateField()
    modified_date = models.DateField()
    user_code = models.TextField()


class user_lecture(models.Model):
    user = models.ForeignKey(user , on_delete=models.CASCADE)
    lecture = models.ForeignKey(lecture , on_delete=models.CASCADE)
