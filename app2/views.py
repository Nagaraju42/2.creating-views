from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app2(request):
    return HttpResponse('this is frist function in app2')


def second_app2(request):
    return HttpResponse('this is second function in app2')