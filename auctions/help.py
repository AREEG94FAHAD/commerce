from django.http import  HttpResponseRedirect
from django.urls import reverse
from functools import wraps


def login_requireed(f):
    def wrapper(*args, **kwargs):
        if args[0].user.is_authenticated:
            return f(*args, **kwargs)
        return HttpResponseRedirect(reverse("login_view"))
    return wrapper

   