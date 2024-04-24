from django.shortcuts import render

# Create your views here.


def index(request):

    context = {}

    return render(request, "home/index.html", context)


def read_more(request):

    context = {}

    return render(request, "home/read_more.html", context)
