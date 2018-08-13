from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from account.forms import SignUpForm


def signup(request):
    print(request)
    if request.method == 'POST':
        print("passed")
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        print("failed")
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


