from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models
import uuid

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Student(AbstractUser):
    username = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100, null=True, blank=True)
    university_year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return self.username


class Project(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    skills_required = models.ManyToManyField('Skill')  # Define before using
    details = models.TextField()

    def __str__(self):
        return self.project_id


class Application(models.Model):
    application_id = models.CharField(max_length=100, primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    applicant_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    application_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.application_id
