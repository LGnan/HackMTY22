from django.shortcuts import render

# Create your views here.

def politica(request):
    
    return render(request, "politica/politica.html")