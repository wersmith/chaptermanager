from django.shortcuts import render
from django.http import HttpResponse


def member(requests):
    return HttpResponse('Member endpoint')
