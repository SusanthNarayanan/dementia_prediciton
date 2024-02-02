from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-predictions')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)


def predictions(request):
    predicted_sports = Data.objects.all()
    context = {
        'predicted_sports': predicted_sports
    }
    return render(request, 'dashboard/predictions.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard-index')  # Updated redirect path
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
            else:
                form.save()
                return redirect('login')  
        else:
            messages.error(request, "Invalid form submission. Please correct the errors.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
