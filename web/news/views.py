from django.shortcuts import render
from .models import Person
from .forms import PersonForm

def news(request):
    return render(request, 'news/news.html')

def create(request):
    form = PersonForm()

    data= {
        'form': form
    }
    return render(request, 'news/create.html')
