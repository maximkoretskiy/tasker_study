# coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from models import Task, TaskAddForm, TaskEditForm

@login_required
def dash(request):
    page_title = 'Список задач'
    week_list = Task.objects.filter(executor_id=request.user.id, level='W')
    month_list = Task.objects.filter(executor_id=request.user.id, level='M')
    quoter_list = Task.objects.filter(executor_id=request.user.id, level='Q')
    return render_to_response('tasks/dash.html', locals() )

def task_delete(request, task_id):
    task = get_object_or_404(Task,pk=task_id)
    task.status = 'A'
    task.save()
    return HttpResponseRedirect(reverse('dashboard'))

def task_edit(request, task_id):
    task = get_object_or_404(Task,pk=task_id)
    page_title = u"Редактирование задачи %s" % task.title
    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = TaskEditForm(instance=task)

    return render_to_response('tasks/add_task.html', RequestContext(request ,locals()) )

def task_status(request, task_id, status):
    task = get_object_or_404(Task,pk=task_id)
    task.complete(status)
    return HttpResponseRedirect(reverse('dashboard'))


def task_add(request):
    page_title = "Создание задачи"
    if request.method == 'POST':
        form = TaskAddForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.executor = request.user
            task.save()
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = TaskAddForm()

    return render_to_response('tasks/add_task.html', RequestContext(request ,locals()) )
