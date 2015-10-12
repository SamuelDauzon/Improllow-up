# coding:utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Count

from projects.models import Project
from tasks.models import Task
from .models import Customer

def detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    project_id_list = Project.objects.filter(
        customer=customer
    ).values_list(
        'id', 
        flat=True
    ).distinct()
    task_list = Task.objects.filter(project__in=project_id_list)
    task_list = task_list.values('project').annotate(
        total=Count('project')
    ).order_by('-total')
    count_task_list = []
    for task in task_list:
        count_task_list.append({
            'total' : task['total'], 
            'project':Project.objects.get(id=task['project'])
        })
    task_list = Task.objects.filter(
        project__in = project_id_list,
        execution_date__isnull = False
    ).order_by('-execution_date')[:8]
    return render(
        request, 
        'customers/detail.html', 
        {
            'customer' : customer,
            'count_task_list' : count_task_list,
            'task_list' : task_list,
        }
    )
