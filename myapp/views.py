from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Todo


@csrf_exempt
def home(request):
    try:
        if request.method == 'POST':
            task = request.POST.get('task', '')
            done = request.POST.get('done_dropdown', '')
            done = done != "False"

            todo = Todo(task=task, done=done)
            todo.save()
        todos = Todo.objects.all()
        return render(request, 'todo.html', {
            'todos': todos,
        })
    except Exception as e:
        print(e)
        return HttpResponse("Hello world!")
