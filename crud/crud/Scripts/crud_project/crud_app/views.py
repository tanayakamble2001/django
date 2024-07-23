from django.shortcuts import render,redirect
from .models import Emp,EmpForm,AccountForm,Account

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_emp(request):
    if request.method == 'POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=EmpForm
        context={'form':f}
        return render(request,'add_employee.html',context)
    
def add_account(request):
    if request.method == 'POST':
        f=AccountForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=AccountForm
        context={'form':f}
        return render(request,'add_account.html',context)
    
def emp_list(request):
    emp1=Emp.objects.all()
    context={'elist':emp1}
    return render(request,'emplist.html',context)