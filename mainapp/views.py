from django.shortcuts import render

def get_mainapp(request):
    return render(request, "mainapp/mainapp.html")
