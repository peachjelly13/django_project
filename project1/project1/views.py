from django.http import HttpResponse
from django.shortcuts import render

"these are methods"
"this is basically what you will see when you hit a url or a route"
def home(request):
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("about page")

def contact(request):
    return HttpResponse("contact us")