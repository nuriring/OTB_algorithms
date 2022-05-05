from django.shortcuts import render

from algorithms.models import Problem

# Create your views here.

def index(request):
    problems = Problem.objects.order_by('-pk')
    context = {
        'problems' : problems,
    }
    return render(request, 'algorithms/index.html', context)