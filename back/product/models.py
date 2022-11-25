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
    created_date = models.DateTimeField(auto_now_add=True)


class assignment(models.Model):
    assignment_id = models.IntegerField(primary_key=True)
    lecture = models.ForeignKey(lecture , on_delete=models.CASCADE)
    title = models.TextField()
    deadline = models.DateTimeField()


class problem(models.Model):
    problem_id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    lecture = models.ForeignKey(lecture , on_delete=models.CASCADE)
    assignment = models.ForeignKey(assignment, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    restriction = models.TextField(null = True)
    skeleton = models.TextField()
    timelimit = models.IntegerField()
    memorylimit = models.IntegerField()

    def opened_testcase(self):
        return testcase.objects.filter(problem=self, isHidden=False )

    def written_code(self):
        return code.objects.filter(problem = self)

class reference(models.Model):
    reference_id = models.IntegerField(primary_key=True)
    title = models.TextField()
    url = models.TextField()
    problem = models.ForeignKey(problem , on_delete=models.CASCADE)

class testcase(models.Model):
    testcase_id = models.AutoField(primary_key=True)
    problem = models.ForeignKey(problem , related_name='testcases', on_delete=models.CASCADE)
    # show number of testcase in that problem
    idx = models.IntegerField()
    isHidden = models.BooleanField()
    input = models.TextField()
    output = models.TextField()


class solution(models.Model):
    solution_id = models.AutoField(primary_key=True)
    problem = models.ForeignKey(problem , on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    answer_code = models.TextField()


class code(models.Model):
    code_id = models.AutoField(primary_key=True)
    problem = models.ForeignKey(problem , related_name='codes', on_delete=models.CASCADE)
    user = models.ForeignKey(user , on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user_code = models.TextField()
    code_idx = models.IntegerField()


class user_lecture(models.Model):
    user = models.ForeignKey(user , on_delete=models.CASCADE)
    lecture = models.ForeignKey(lecture , on_delete=models.CASCADE)

class session(models.Model):
    session_id = models.AutoField(primary_key=True)
    created_date = models.DateField(auto_now_add=True)
    submission_count = models.IntegerField()
    problem = models.ForeignKey(problem, on_delete=models.CASCADE)
    user = models.ForeignKey(user , on_delete=models.CASCADE)
