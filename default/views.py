from django.shortcuts import render

def home(request):
    return render(request, 'default/home.html', {})

# Create your views here.
