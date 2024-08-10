from django.shortcuts import render,redirect
from .models import Expense,ExpenseForm
from django.contrib.auth.models import User

# Create your views here.
def add_expense(request):
    uid=request.session.get('uid')
    if request.method == 'POST':
        #f=ExpenseForm(request.POST)
        #f.save()
        expense=request.POST.get('expense')
        expense_type=request.POST.get('expense_type')
        description=request.POST.get('description')
        exp=Expense()
        exp.expense=expense
        exp.expense_type=expense_type
        exp.description=description
        exp.user=User.objects.get(id=uid)
        exp.save()
        return redirect('/')
    else:
        f=ExpenseForm
        context={'form':f}
        return render(request,'addexpense.html',context)
    
def expense_list(request):
    #uid=request.session.get('uid')
    #exp=Expense.objects.all()
    #exp=Expense.objects.filter(user=uid)
    #context={'exlist':exp}
    #return render(request,'explist.html',context)
    uid=request.session.get('uid')
    exp=Expense.objects.filter(user=uid)
    expt=set()
    for i in exp:
        expt.add(i.expense_type)
    context={'exp':exp,'expt':expt}
    return render(request,'explist.html',context)

def delete_exp(request,eid):
    exp=Expense.objects.get(id=eid)
    exp.delete()
    return redirect('/expenselist')

def edit_exp(request,eid):
    exp=Expense.objects.get(id=eid)
    if request.method == 'POST':
        f=ExpenseForm(request.POST,instance=exp)
        f.save()
        return redirect('/expenselist')
    else:
        f=ExpenseForm(instance=exp)
        context={'form':f}
        return render(request,'addexpense.html',context)
    
def exp_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    exp=Expense.objects.filter(user=uid,description__contains=srch)
    context={'exp':exp}
    return render(request,'explist.html',context)

def sort_by_expense_type(request,ext2):
    uid=request.session.get('uid')
    exp=Expense.objects.filter(user=uid)
    expt=set()
    for i in exp:
        expt.add(i.expense_type)
        exp=Expense.objects.filter(user=uid,expense_type=ext2)
    context={'exp':exp,'expt':expt}
    return render(request,'explist.html',context)