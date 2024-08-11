from django.shortcuts import render

# Create your views here.

def newapp(request):
    return render(request,'newapp/new_app.html')