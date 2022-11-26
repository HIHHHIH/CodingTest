from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(lecture)
admin.site.register(user)
admin.site.register(assignment)
admin.site.register(problem)
admin.site.register(testcase)
admin.site.register(solution)
admin.site.register(code)
admin.site.register(user_lecture)
admin.site.register(session)
admin.site.register(reference)