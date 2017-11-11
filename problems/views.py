from django.shortcuts import render
from .functions import LIST_PROBLEMS
from random import randint
# Create your views here.


def problems(request):
    random_numbre = randint(0,len(LIST_PROBLEMS)-1)
    problema = LIST_PROBLEMS[random_numbre]
    return render(request, 'index.html', problema)
