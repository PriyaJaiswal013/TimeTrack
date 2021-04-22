from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    project_names=models.CharField(max_length =150)
    status =models.BooleanField(default=True)

    def __str__(self):
        return self.project_names

    class Meta:
        verbose_name ="project name"
        verbose_name_plural="projects"

class UserTasks(models.Model):
    employee =models.ForeignKey(User, on_delete=models.CASCADE)
    Task_title = models.CharField(max_length=100)
    start_time =models.CharField(max_length=60)
    end_time =models.CharField(max_length=60,blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.Task_title

    class Meta:
        verbose_name ="Task"
        verbose_name_plural="Task Names"
    