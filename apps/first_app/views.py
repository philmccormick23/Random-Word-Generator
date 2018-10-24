from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string

# the index function is called when root is visited

def index(request):
    context = {
        'word': get_random_string(length=14)
    }
    if 'number' not in request.session:
        request.session['number']=1
    
    return render(request, 'random_word/page.html', context)

def count(request):
    request.session['number']+=1
    
    return redirect('/')
