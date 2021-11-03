from django.contrib import admin
from .models import ToDoList, Person, Task

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Person)
admin.site.register(Task)