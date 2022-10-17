from django.shortcuts import render
from django.http import HttpResponse


def kuy(request) :
    # return HttpResponse('kuypage')
    return render(request,"index.html")
