from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'New'
        IN_PROGRESS = 'In Progress'
        DONE = 'Done'

    class Priority(models.IntegerChoices):
        LOW = 1, 'Low'
        MEDIUM = 2, 'Medium'
        HIGH = 3, 'High'

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW)
    due_date = models.DateField(blank=True, null=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')    
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   


    def __str__(self):
        return self.title
    

class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='projects', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name