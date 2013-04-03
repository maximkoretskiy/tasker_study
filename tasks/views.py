# coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from models import Task, Project, TaskAddForm, TaskEditForm
from tasker.common import class_view_decorator


@login_required
def dash(request):
    page_title = 'Список задач'
    week_list = Task.objects.filter(executor_id=request.user.id, level='W')
    month_list = Task.objects.filter(executor_id=request.user.id, level='M')
    quoter_list = Task.objects.filter(executor_id=request.user.id, level='Q')
    return render_to_response('tasks/dash.html', locals() )

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task,pk=task_id)
    task.status = 'A'
    task.save()
    return HttpResponseRedirect(reverse('dashboard'))

@login_required
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

@login_required
def task_status(request, task_id, status):
    task = get_object_or_404(Task,pk=task_id)
    task.complete(status)
    return HttpResponseRedirect(reverse('dashboard'))

@login_required
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


def _change_context(parent,**kwargs):
    context = super(parent.__class__, parent).get_context_data(**kwargs)
    context['page_title'] = parent.page_title
    return context

@class_view_decorator(login_required)
class ProjectList(ListView):
    model = Project
    page_title = "Список проектов"
    get_context_data = _change_context

@class_view_decorator(login_required)
class ProjectCreate(CreateView):
    model = Project
    success_url = reverse_lazy('project_list')
    page_title = "Создание проекта"
    get_context_data = _change_context


@class_view_decorator(login_required)
class ProjectUpdate(UpdateView):
    model = Project
    success_url = reverse_lazy('project_list')
    page_title = "Редактирование проекта"
    get_context_data = _change_context


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return HttpResponseRedirect(reverse('project_list'))
