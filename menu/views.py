from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.

class ADD(forms.Form):
    do = forms.CharField()
def index(request):
    if 'task' not in request.session:
        request.session['task'] = []
    return render(request, 'index.html', {
        "form": ADD(),
        "task": request.session['task']
    })

def add(request):
    if request.method == "POST":
        form = ADD(request.POST)
        if form.is_valid():
            request.session['task'] += [form.cleaned_data['do']]
            return HttpResponseRedirect(reverse('index'))

def remove(request):
    if request.method == "POST":
        request.session.pop('task')
        return HttpResponseRedirect(reverse('index'))