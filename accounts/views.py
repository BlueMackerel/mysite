from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login
from accounts.forms import  UserForm
# Create your views here.


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('bookswiki:index')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})
