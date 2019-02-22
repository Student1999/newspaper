from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def single_post(request):
    return render(request, 'single-post.html')

def about(request):
    return render(request, 'about.html')

def catagories_post(request):
    return render(request, 'catagories-post.html')