from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Post
# Create your views here.

# class BlogListView(ListView):
#     model=Post
#     template_name='home.html'

def BlogListView(request):
    post=Post.objects.filter(author_id=1)
    return render(request,'home.html',{'posts':post})
def BlogDetailView(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'detail.html',{'posts':post})
