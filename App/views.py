from django.shortcuts import render,redirect
from App.form import TODODF
from App.models import TODOM


# Create your views here.
def index(request):
    obj = TODOM.objects.all()
    context ={
        'listout' : obj,
        'form' : TODODF
    }
    return render(request,'App/index.html',context)

def createTask(request):

    if request.POST:
        obj = TODODF(request.POST)
        if obj.is_valid():
            obj.save()
    return redirect('index')

def DeleteTask(request,pkk):
    obj = TODOM.objects.get(id=pkk)
    obj.delete()
    return redirect('index')

def UpdateTask(request,pkk):
    obj = TODOM.objects.get(id=pkk)
    ff = TODODF(instance=obj)
    context = {'form' : ff}
    if request.POST:
        kk = TODODF(request.POST,instance=obj)
        if kk.is_valid():
            kk.save()
            return redirect('index')

    return render(request,'App/update.html',context)