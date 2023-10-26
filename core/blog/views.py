from typing import Any
from django.shortcuts import render
from django.views import View
from .models import *
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

class indexView(View):
    def get(self, request):
        post = Post.objects.all()
        return render(request, 'blog/index.html', {'post':post})

class IndexPostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/detail.html', {'post':post})
    
# class IndexView(TemplateView):
#     template_name = 'blog/index.html'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         context['post'] = Post.objects.all()
#         return context


class IndexRedirect(RedirectView):
    url = 'blog:redirect'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)