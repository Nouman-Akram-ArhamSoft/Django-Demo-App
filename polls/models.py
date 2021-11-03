from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE

# Create your models here.

class Person(models.Model):
    person_name = models.CharField(max_length=100)
    person_DOB = models.DateField(blank=True)
    person_address = models.TextField(blank=True)

    def __str__(self):
        return self.person_name


class ToDoList(models.Model):
    list_name = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.list_name}"


class Task(models.Model):
    task_title = models.CharField(max_length=100, blank=False, unique=True)
    start_time = models.DateTimeField(default=datetime.now())
    is_complete = models.BooleanField(default=False)
    end_time = models.DateTimeField(blank=True)
    task_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task_title}"