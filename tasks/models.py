# coding=utf-8
from django.db import models
from django.forms import ModelForm, DateInput,Textarea
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput
from django.contrib.auth.models import User
from datetime import date

TASK_LEVEL_CHOICES = (
    ('W', u'Week'),
    ('M', u'Month'),
    ('Q', u'Quoter')
)

TASK_STATUS_CHOICES = (
    ('C', u'Создана'),
    ('R', u'Выполнена'),
    ('A', u'Помещена в архив')
)


class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True,)
    level = models.CharField(max_length=1, choices=TASK_LEVEL_CHOICES)
    status = models.CharField(max_length=1, choices=TASK_STATUS_CHOICES, default='C')
    comment = models.CharField(max_length=200, blank=True)
    executor = models.ForeignKey(User)
    project = models.ForeignKey('Project')

    def complete(self, flag):
        if self.status == 'A':
            return
        if flag is True:
            self.status = 'R'
            self.finish_date = date.today()
        else:
            self.status = 'C'
            self.finish_date = None
        self.save()


class Project(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class TaskAddForm(ModelForm):
    class Meta:
        model = Task
        fields = ('project', 'title', 'due_date','level')
        widgets = {
            'due_date': BootstrapDateInput(format='%d.%m.%Y'),
        }


class TaskEditForm(ModelForm):
        class Meta:
            model = Task
            fields = ('project', 'title', 'due_date','level', 'comment')
            widgets = {
                'due_date': BootstrapDateInput(format='%d.%m.%Y'),
                'finish_date': BootstrapDateInput(format='%d.%m.%Y'),
                'comment': Textarea()
            }
