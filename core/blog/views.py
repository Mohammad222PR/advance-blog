from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class indexView(View):
    def get(self, request):
        post = Post.objects.all()
        return render(request, 'blog/index.html', {'post':post})

class IndexPostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/detail.html', {'post':post})