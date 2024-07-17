from django.shortcuts import render,HttpResponse
#def home(request):
#    return HttpResponse('<h1>Welcome to django</h1>')
def home(request):
    return render(request,'home.html')
def first_page(request):
    return render(request,'first.html')
def second_page(request):
    return render(request,'second.html')
# Create your views here.
