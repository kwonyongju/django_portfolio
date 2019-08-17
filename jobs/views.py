from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detail_blog})
