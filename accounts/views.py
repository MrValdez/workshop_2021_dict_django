# templates suggestion:
#  https://github.com/macdhuibh/django-registration-templates

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
#        instance = User()
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
#            instance.user_permissions.add("forum.view_post")

            return redirect("/account/success_account_create")
    else:
        form = UserCreationForm()
        
    return render(request, "registration/register.html", {'form': form})