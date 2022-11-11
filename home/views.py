from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("this si index page")
    return render(request,'index.html')

def about(request):
    #return HttpResponse("this is about page")
    return render(request,'about.html')

def services(request):
    #return HttpResponse("this si services page")
    return render(request,'services.html')

def contact(request):
    #return HttpResponse("this si contact page")
    return render(request,'contact.html')

