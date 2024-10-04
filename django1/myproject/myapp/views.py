from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home Page</h1><p>Welcome to the home page!</p>")

def about(request):
    return HttpResponse("<h1>About Page</h1><p>This is the about page.</p>")
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home Page</h1><p>Welcome to the home page!</p>")

def about(request):
    return HttpResponse("<h1>This is About Page</h1><p>I am Arun currently doing my ug in kamaraj college. my areas of interest are flutter and iot.</p>")
