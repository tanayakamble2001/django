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


def delete_emp(request):
    eid = request.GET.get('id')
    emp = Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/emplist')

def delete2_emp(request,eid):
    emp=Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/emplist')

def edit_emp(request,eid):
    emp=Emp.objects.get(id=eid)
    if request.method == 'POST':
        f=EmpForm(request.POST,instance=emp)
        f.save()
        return redirect('/emplist')
    else:
        f=EmpForm(instance=emp)
        context={'form':f}
        return render(request,'add_employee.html',context)
    
def account_list(request):
    acc1=Account.objects.all()
    context={'aclist':acc1}
    return render(request,'acclist.html',context)

def delete_acc(request):
    aid = request.GET.get('id')
    acc = Account.objects.get(id=aid)
    acc.delete()
    return redirect('/acclist')

def delete2_acc(request,aid):
    acc=Account.objects.get(id=aid)
    acc.delete()
    return redirect('/acclist')

def edit_acc(request,aid):
    acc=Account.objects.get(id=aid)
    if request.method == 'POST':
        f=AccountForm(request.POST,instance=acc)
        f.save()
        return redirect('/acclist')
    else:
        f=AccountForm(instance=acc)
        context={'form':f}
        return render(request,'add_account.html',context)
