from django.contrib import admin
from .models import Student, Skill, Project, Application
# Register your models here.

admin.site.register(Student)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Application)
