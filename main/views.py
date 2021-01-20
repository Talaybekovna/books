from django.shortcuts import render, HttpResponse, redirect

def homepage(request):
    return HttpResponse("Homepage")
