# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import Task, TaskAddForm

@login_required
def dash(request):
    form  = TaskAddForm()
    week_list = Task.objects.filter(executor_id=request.user.id, level='W')
    month_list = Task.objects.filter(executor_id=request.user.id, level='M')
    quoter_list = Task.objects.filter(executor_id=request.user.id, level='Q')
    return render_to_response('tasks/dash.html', locals() )

def task_add(request):
    if request.method == 'GET':
        data = request.GET.copy()
        data.appendlist('executor', request.user.id)
        data.appendlist('status', 'C')
        form = TaskAddForm(data)
        if form.is_valid():
            print 'saving data'
            form.save()
        else:
            pass
        #assert False
        return render_to_response('tasks/dash.html', RequestContext(request ,locals()) )
