from django.http import HttpResponse

"these are methods"
"this is basically what you will see when you hit a url or a route"
def home(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("about page")

def contact(request):
    return HttpResponse("contact us")