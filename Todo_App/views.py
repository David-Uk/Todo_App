from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'main/index.html')


@csrf_exempt
def add_todo(request):
    print(request.POST)
    return render(request, 'main/index')
