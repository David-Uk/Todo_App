from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import ToDo
from django.http import HttpResponseRedirect


def home(request):
    todo_items = ToDo.objects.all().order_by('added_date')
    return render(request, 'main/index.html', {
        'todo_items': todo_items
    })


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']
    created_obj = ToDo.objects.create(added_date=current_date, text=content)
    print(created_obj)
    length_of_list = ToDo.objects.all().count()
    print(length_of_list)
    return HttpResponseRedirect('/')


@csrf_exempt
def delete_todo(request, todo_id):
    print(todo_id)
    ToDo.objects.get(id=todo_id)
    return HttpResponseRedirect('/')
