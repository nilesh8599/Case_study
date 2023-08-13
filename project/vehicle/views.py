from django.shortcuts import render , redirect 
from .models import vehicle
 
# Create your views here.

def index(request):
    data=vehicle.objects.all()
    print(data)
    context ={'data':data}
    return render(request , 'index.html' , context)


def insertdata(request):
  
    if request.method=='POST':
        name =request.POST.get('name')
        model =request.POST.get('model')
        description =request.POST.get('description')
        type =request.POST.get('type')
        print(name , model , description , type  )
        query =vehicle (name = name , model=model , description=description , type = type )
        query.save()
        return redirect ('/')
    
    
    return render (request , 'index.html' )


def updatedata(request , id):
    if request.method=='POST':
        name =request.POST['name']
        model =request.POST['model']
        description =request.POST['description']
        type =request.POST['type']
        edit=vehicle.objects.get(id=id)
        edit.name=name
        edit.model=model
        edit.description=description
        edit.type=type
        edit.save()
       
        return redirect ('/')
        
    d=vehicle.objects.get(id=id)
    context ={'d':d}
    return render(request , 'edit.html' , context)

def deletedata(request ,id ):
    d=vehicle.objects.get(id=id)
    d.delete()
    return redirect('/')