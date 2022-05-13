from calendar import c
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from algorithms.models import Problem, Solution
from .forms import ProblemForm, SolutionForm, CommentForm
from django.http import JsonResponse, HttpResponse

# Create your views here.

def problem_index(request):
    problems = Problem.objects.order_by('-pk')
    context = {
        'problems' : problems,
    }
    return render(request, 'algorithms/problem_index.html', context)


def problem_create(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('algorithms:problem_index')
    else:
        form = ProblemForm()
    context = {
        'form':form,
    }
    return render(request, 'algorithms/problem_create.html', context)

def problem_detail(request, problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    context = {
        'problem': problem,
    }
    return render(request, 'algorithms/problem_detail.html', context)

def problem_update(request, problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    if request.method == 'POST':
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return redirect('algorithms:problem_detail', problem_pk)
    else:
        form = ProblemForm(instance=problem)
    context = {
        'problem': problem,
        'form': form,
    }
    return render(request, 'algorithms/problem_update.html', context)

def problem_delete(request, problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    if request.method == "POST":
        problem.delete()
        return redirect('algorithms:problem_index')
    return redirect('algorithms:problem_detail', problem.pk)

def solution_index(request, problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    solutions = problem.solution_set.order_by('-like_users')
    comment_form = CommentForm()
    context = {
        'solutions' : solutions,
        'problem' : problem,
        'comment_form' : comment_form
    }
    return render(request, 'algorithms/solution_index.html', context)

def solution_create(request, problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.user = request.user
            solution.problem = problem
            solution.save()
        return redirect('algorithms:solution_index', problem.pk)
    else:
        form = SolutionForm()
    context = {
        'form': form,
        'problem': problem,
    }
    return render(request, 'algorithms/solution_create.html', context)

def solution_update(request, problem_pk, solution_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    solution = get_object_or_404(Solution, pk=solution_pk)
    if request.user == solution.user:
        if request.method == 'POST':
            form = SolutionForm(request.POST, instance=solution)
            if form.is_valid():
                form.save()
                return redirect('algorithms:solution_index', problem.pk)
        else:
            form = SolutionForm(instance=solution)
    else:
        return redirect('algorithms:solution_index', problem.pk)
    context = {
        'problem': problem,
        'form': form,
    }
    return render(request, 'algorithms/solution_update.html', context)

def solution_delete(request, problem_pk, solution_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    solution = get_object_or_404(Solution, pk=solution_pk)
    if request.user.is_authenticated:
        if request.user == solution.user:
            solution.delete()
    return redirect('algorithms:solution_index', problem.pk)

def solution_comment(request, problem_pk, solution_pk):
    if request.user.is_authenticated:
        problem = get_object_or_404(Problem, pk=problem_pk)
        solution = get_object_or_404(Solution, pk=solution_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.solution = solution
            comment.save()
        return redirect('algorithms:solution_index', problem.pk)
    return redirect('accounts:signin')

def solution_like(request, problem_pk, solution_pk):
    if request.user.is_authenticated:
        problem = get_object_or_404(Problem, pk=problem_pk)
        solution = get_object_or_404(Solution, pk=solution_pk)
        if solution.like_users.filter(pk=request.user.pk).exists():
            solution.like_users.remove(request.user)
            liked = False
        else:
            solution.like_users.add(request.user)
            liked = True
        context = {
            'liked': liked,
            'count': solution.like_users.count()
        }
        return JsonResponse(context)
    return HttpResponse(status=401)