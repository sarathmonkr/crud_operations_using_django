from django.shortcuts import redirect, render
from django.http import HttpResponse
from todoapp.form import ToDoForm
from todoapp.models import ToDo
# Create your views here.

def index(request):
    form=ToDoForm()
    #to get all values
    todos=ToDo.objects.all()
    
    #to store values to db
    if request.method =='POST':
        form=ToDoForm(request.POST)
        if form.is_valid():
            form.save()    
    return render(request,'index.html',{'form':form,'todos':todos})

def update(request,todo_id):
    todo=ToDo.objects.get(id=todo_id)
    form=ToDoForm(instance=todo)
    if request.method=='POST':
        form=ToDoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'update.html',{'form':form})


def delete(request,todo_id):
    todo_del=ToDo.objects.get(id=todo_id)    
    todo_del.delete()
    return redirect('index')
    