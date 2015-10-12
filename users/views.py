# coding:utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from tasks.models import Task
from .models import UserProfile
from .forms import FormConnection

def connection(request):
    """
    Cette view permet aux utilisateurs de se connecter
    """
    form = FormConnection() 
    if request.POST:
        form = FormConnection(request.POST) 
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if request.GET.get('next') is not None:
                    return HttpResponseRedirect(reverse(request.GET['next']))
                else:
                    return HttpResponseRedirect(reverse('users:list'))
    return render(request, 'users/connection.html', {'form' : form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def detail(request, pk):
    userprofile = get_object_or_404(UserProfile, pk=pk)
    task_list = Task.objects.filter(
        Q(userprofile=userprofile) | 
        Q(user_add=userprofile)
    )
    paginator = Paginator(task_list, 10)
    page = request.GET.get('page')
    try:
        task_list_page = paginator.page(page)
    except PageNotAnInteger:
        task_list_page = paginator.page(1)
    except EmptyPage:
        task_list_page = paginator.page(paginator.num_pages)
    task_to_do = Task.objects.filter(
        userprofile = userprofile,
        execution_date__isnull = True
    ).order_by('-execution_date')[:10]
    return render(
        request, 
        'users/detail.html', 
        {
            'userprofile' : userprofile,
            'task_list_page' : task_list_page,
            'task_to_do' : task_to_do,
        }
    )
