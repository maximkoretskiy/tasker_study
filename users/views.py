# Create your views here.
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect


def login_or_redirect(request, template_name='users/login.html', redirect_to='/'):
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    else:
        return login(request, template_name)