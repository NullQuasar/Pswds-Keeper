from django.shortcuts import render, redirect
from .models import Session
from .forms import SessionForm

def home(request):
    return render(request, 'home.html')

def add_new(request):
    if request.method == 'POST':
        session_form = SessionForm(request.POST)
        if session_form.is_valid():
            session_form.save()
            return redirect('add')

    session_form = SessionForm()
    return render(request, 'add-new.html', {'form': session_form})

def about(request):
    return render(request, 'about.html')

def passwords(request):
    Sessions = Session.objects.all()
    print(Sessions)
    return render(request, 'passwords.html', {'sessions': Sessions})