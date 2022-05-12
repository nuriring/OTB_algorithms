from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from algorithms.models import Problem, Solution
from .forms import ProblemForm
from django.db.models import Q

# Create your views here.

def index(request):
    problems = Problem.objects.order_by('-pk')
    levels = ['브', '실', '골', '플']
    context = {
        'problems' : problems,
        'levels' : levels,
    }
    return render(request, 'algorithms/index.html', context)


def create(request):
    # if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('algorithms:index')
        else:
            form = ProblemForm()
        context = {
            'form':form,
        }
        return render(request, 'algorithms/create.html', context)

def detail(request, problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    context = {
        'problem': problem,
    }
    return render(request, 'algorithms/detail.html', context)

def problem_update(request, problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    # if request.method == 'POST':
    form = ProblemForm(request.POST, instance=problem)
    if form.is_valid():
        form.save()
        return redirect('algorithms:detail', problem_pk)
    else:
        form = ProblemForm(instance=problem)
    context = {
        'problem': problem,
        'form': form,
    }
    return render(request, 'algorithms/update.html', context)


def problem_delete(request, problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    if request.method == "POST":
        problem.delete()
        return redirect('algorithms:index')
    return redirect('algorithms:detail', problem.pk)

def solution_index(request, problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    solutions = problem.solution_set.all()
    #솔루션 마다 댓글 출력하기
    
    

    context = {
        'solutions' : solutions,
        'problem' : problem,
    }
    return render(request, 'algorithms/solution.html', context)


def problem_search(request):
    problems = Problem.objects.all()
    f_levels = request.GET.getlist('f')
    if f_levels: #filtered level이 존재한다면
        query = Q()
        for f_level in f_levels:
            query = query | Q(level__icontains=f_level)
            f_problems = problems.filter(query).order_by('-pk')


    context = {
        'f_problems' : f_problems
    }
    return render(request, 'algorithms/search.html', context)