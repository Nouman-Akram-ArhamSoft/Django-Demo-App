from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import ToDoList, Person, Task
# Create your views here.

def get_person(person_id):
    try:
        obj = Person.objects.get(pk=person_id)
        return obj
    except Person.DoesNotExist:
        raise Http404("Person Does Not Exits.")

def get_todo_task(todo_id):
    try:
        obj = ToDoList.objects.get(pk=todo_id)
        return obj
    except ToDoList.DoesNotExist:
        raise Http404("List not Found")

def index(request):

    person_list = Person.objects.all()
    persons_dictonary = {'person_list': person_list}
    return render(request, 'polls/index.html', persons_dictonary)


def show_specific_person(request, person_id):


    required_list = [todo_list for todo_list in ToDoList.objects.all(
    ) if todo_list.owner.id == person_id]
    return render(request, 'polls/todo_list.html', {
        'list_detail': required_list,
        'owner': get_person(person_id)
        })


def show_specific_todo_list(request, todo_id):

    task_details = [task_list for task_list in Task.objects.all(
    ) if task_list.task_list.id == todo_id]

    return render(request, 'polls/task_list.html', 
                  {"task_list": task_details,
                   'task_name': get_todo_task(todo_id)})
