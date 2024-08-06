from django.shortcuts import render
from django.views.generic import FormView,CreateView,ListView

from .models import EmpForm,Emp

# Create your views here.
def home(request):
    return render(request,'home.html')

class EmpRegister(FormView):
    form_class=EmpForm
    template_name='addemp.html'

class add_emp(CreateView):
    model=Emp
    fields='__all__'
    success_url='/'

class emp_list(ListView):
    model=Emp
    template_name='emplist.html'