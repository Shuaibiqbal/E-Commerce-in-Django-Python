from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Index Shop")
    return render(request, "shop/index.html")

def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("search")

def productview(request):
    return HttpResponse("prodview")
def checkout(request):
    return HttpResponse("checkout")