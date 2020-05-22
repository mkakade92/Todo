from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from .models import task as T
# Create your views here.

from .forms import TaskForm, UpdateTaskForm

def TaskDetail(request,pk):
    task = get_object_or_404(T,pk=pk)

    context = {
        'task' : task,
        'title':str(task.title),
    }

    return render(request,'tasks/task_detail.html',context)

def CreateTask(request):
    tasks = T.objects.all()
    
    form = TaskForm()


    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {
        'tasks' : tasks,
        'title':"TaskLisT",
        'form':form
    }
    return render(request,'tasks/tasklist.html',context)

def UpdateTask(request,pk):
    task = get_object_or_404(T,pk=pk)
    form = UpdateTaskForm(instance=task)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_detail",pk)

    context = {
        'task':task,
        'form':form,
        'title':"Update "+str(task.title)
    }
    return render(request,'tasks/update_task.html',context)


def DeleteTask(request,pk):
    task = get_object_or_404(T,pk=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect("index")

    context = {
        'task':task,
        'title':"Delete "+str(task.title)
    }

    return render(request,'tasks/confirm_delete_task.html',context)