from django.urls import path
from . import views
app_name = 'algorithms'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:problem_pk>/', views.detail, name='detail'),
    path('<int:problem_pk>/update/', views.problem_update, name='problem_update'),
    path('<int:problem_pk>/delete/', views.problem_delete, name='problem_delete'),
    path('<int:problem_pk>/solution/', views.solution_index, name='solution'),
]