from django.shortcuts import redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse


# Create your views here.
def index(request):
    if (request.user is None) or not request.user.is_authenticated:
        return redirect_to_login(request.get_full_path())

    context = {
        "user": request.user,
        "logout_url": reverse("auth-logout")
    }

    template = loader.get_template("dashboard/index.html")

    return HttpResponse(template.render(context, request))
