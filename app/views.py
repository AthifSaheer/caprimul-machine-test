from django.shortcuts import render, redirect
from .models import *

def home(request):
    todos = Todo.objects.all().order_by('-id')

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            todo = Todo()
            todo.text = text
            todo.save()
        else:
            return render(request, 'home.html', {'error': "This fields is required!", 'todos': todos})

    return render(request, 'home.html', {'todos': todos})

def edit(request, id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=id)
            return render(request, 'home.html', {'todo': todo})
        except Todo.DoesNotExist:
            return render(request, 'home.html', {'error': "Something went wrong!"})

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            try:
                todo = Todo.objects.get(id=id)
            except Todo.DoesNotExist:
                return render(request, 'home.html', {'error': "Something went wrong!"})
                
            todo.text = text
            todo.save()
            return redirect('home')
        else:
            return render(request, 'home.html', {'error': "This fields is required!"})

def delete(request, id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return render(request, 'home.html', {'error': "Something went wrong!"})
        todo.delete()
        return redirect('home')

def finished(request, id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return render(request, 'home.html', {'error': "Something went wrong!"})
        todo.done = True
        todo.save()
        return redirect('home')


