from django.shortcuts import render
from .models import dolls
from django.http import HttpResponse
# Create your views here.
def posts_list(request):
    dog = dolls.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'dolls': dog})

def rats(request, slug):
    cat = dolls.objects.get(slug=slug)
    return render(request, 'posts/eats.html', {'dolls': cat})