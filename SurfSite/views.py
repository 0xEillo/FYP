from django.shortcuts import render

def home(request):
    return render(request, 'Surfsite/home.html')

def llangenith(request):
    return render(request, 'SurfSite/beaches/llangenith.html')
