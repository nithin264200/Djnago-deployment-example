from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'Hello! Nithin', 'number':264}
    return render(request, 'index.html' , context_dict)

def others(request):
    return render(request, 'others.html')

def relative(request):
    return render(request, 'relative_url_template.html')

