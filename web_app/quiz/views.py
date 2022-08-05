from django.shortcuts import render
from . import models


def index(request):
    return render(request, 'quiz/index.html')
