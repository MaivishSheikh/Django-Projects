from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # name = user.name
    context = {
        'name': 'Nahida',
        'country': 'Teyvat',
        'element': 'Dendro',
    }
    return render(request, 'index.html', context)  # Render the index template with context

def register(request):
    name = request.GET['name']
    country = request.GET['country']
    element = request.GET['element']
    archon = request.GET['archon']
    word_count = len(archon.split())
    context = {
        'name': name,
        'country': country,
        'element': element,
        'word_count': word_count
    }
    return render(request, 'register.html', context)
