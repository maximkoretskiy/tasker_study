# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from models import Task, TaskAddForm

@login_required
def dash(request):
    week_list = Task.objects.filter(executor_id=request.user.id, level='W')
    month_list = Task.objects.filter(executor_id=request.user.id, level='M')
    quoter_list = Task.objects.filter(executor_id=request.user.id, level='Q')
    return render_to_response('tasks/dash.html', locals() )

def task_add(request):
    if request.method == 'POST':
        form = TaskAddForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.executor = request.user
            task.save()
            return HttpResponseRedirect(reverse('dashboard'))

        else:
            pass
        #assert False
    else:
        form = TaskAddForm()

    return render_to_response('tasks/add_task.html', RequestContext(request ,locals()) )
