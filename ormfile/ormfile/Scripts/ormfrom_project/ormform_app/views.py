from django.shortcuts import render,redirect
from .models import EmpForm
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
        context= {'form':f}
        return render(request,'addemp.html',context)