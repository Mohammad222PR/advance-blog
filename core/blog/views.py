from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import *
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import *
from django.urls import reverse_lazy
# Create your views here.

# class PostView(View):
#     def get(self, request):
#         posts = Post.objects.all()
#         return render(request, 'blog/index.html', {'posts':posts})


# class IndexPostDetail(View):
#     def get(self, request, pk):
#         post = Post.objects.get(id=pk)
#         return render(request, 'blog/detail.html', {'post':post})
    
# # class IndexView(TemplateView):
# #     template_name = 'blog/index.html'

# #     def get_context_data(self, **kwargs):
# #         # Call the base implementation first to get a context
# #         context = super().get_context_data(**kwargs)
# #         context['post'] = Post.objects.all()
# #         return context


# # class IndexRedirect(RedirectView):
# #     url = 'blog:redirect'

# #     def get_redirect_url(self, *args, **kwargs):
# #         return super().get_redirect_url(*args, **kwargs)


class PostView(ListView):
    template_name = 'blog/index.html'
    queryset = Post.objects.filter(status=True)
    paginate_by = 1
    ordering = '-id'  
    context_object_name = 'posts'
    

class IndexPostDetail(DetailView):
    template_name = 'blog/detail.html'
    model = Post
    context_object_name = 'post'
    

# class PostCreateView(FormView):
#     template_name = 'blog/post_create.html'
#     form_class = PostCreateForm
#     success_url = '/blog/'

#     def form_valid(self, form):
#         new_post=form.save(commit=False)
#         new_post.author = self.request.user
#         new_post.status = True
#         new_post.save()
#         return super().form_valid(form)
    


class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    model = Post
    fields = ['title','content','category','tag','image']
    success_url = reverse_lazy('/blog/')
    
    def form_valid(self, form):
        new_post=form.save(commit=False)
        new_post.author = self.request.user
        new_post.status = True
        new_post.save()
        return super().form_valid(form)
    

class PostUpdateView(UpdateView):
    template_name = 'blog/post_create'
    model = Post
    form_class = PostCreateForm
    success_url = '/blog/'



class DeletePostView(DeleteView):
    template_name = 'blog/delete.html'
    model = Post
    success_url = '/blog/'