from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def reg(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('push:dise')
    else:
        form = UserCreationForm()
    return render(request, 'direc/ones.html', {'form':form})
def login_view(request):
    if request.method == "POST":
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            login(request, forms.get_user())
            return redirect('push:dise')
    else:
        forms = AuthenticationForm()
    return render(request, 'direc/two_log.html', {'form':forms})
