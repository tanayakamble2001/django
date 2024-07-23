from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def first_page(request):
    return render(request,'first.html')