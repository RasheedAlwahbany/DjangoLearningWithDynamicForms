from django.shortcuts import render
from djangoApp1.models import usersN
from djangoApp1.forms import userNForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    context = {'user':usersN.objects.all()}

    return render(request,'about.html',context)

def addUser(request):
    name=''
    id=''
    if request.method=='POST':
        if request.POST['option']=='Add' or request.POST['option']=='Edit':
            if request.POST['option']=='Add':
                n=usersN(name=request.POST['name'])
            elif request.POST['option']=='Edit':
                n=usersN.objects.get(id=request.POST['id'])
                n.name=request.POST['name']
            n.save()
        elif request.POST['option']=='Delete':
            n=usersN.objects.get(id=request.POST['id'])
            n.delete()
        elif request.POST['option']=='Search':
            n=usersN.objects.get(id=request.POST['id'])
            id=n.id
            name=n.name

    context = {'user': usersN.objects.all(),'name':name,'id':id}
    return render(request,'add_user.html',context)

def dynamicForm(request):
    form=userNForm();
    if request.method=='POST':
        form=userNForm(request.POST)
        if form.is_valid():
            if request.POST['option']=='Add' or request.POST['option']=='Edit':
                if request.POST['option']=='Add':
                    n=usersN(name=form.cleaned_data['name'])

                elif request.POST['option']=='Edit':
                    n=usersN.objects.get(id=request.POST['id'])
                    n.name=form.cleaned_data['name']
                n.save()
            elif request.POST['option']=='Delete':
                n=usersN.objects.get(id=request.POST['id'])
                n.delete()
        elif request.POST['option']=='Search':
            n=usersN.objects.get(id=request.POST['id'])
            form=userNForm(n)


    context = {'form':form,'user': usersN.objects.all()}
    return render(request,'add_user_dynamic_form.html',context)