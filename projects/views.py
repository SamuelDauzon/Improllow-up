# coding:utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from users.models import UserProfile
from tasks.models import Task
from .models import Project

def detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    task_list = Task.objects.filter(project=project)
    paginator = Paginator(task_list, 50)
    page = request.GET.get('page')
    try:
        task_list_page = paginator.page(page)
    except PageNotAnInteger:
        task_list_page = paginator.page(1)
    except EmptyPage:
        task_list_page = paginator.page(paginator.num_pages)
    last_task_list = Task.objects.filter(
        project = project,
        execution_date__isnull = False
    ).order_by('-execution_date')[:8]
    return render(
        request, 
        'projects/detail.html', 
        {
            'project' : project,
            'task_list_page' : task_list_page,
            'last_task_list' : last_task_list,
        }
    )
