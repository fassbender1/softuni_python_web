from datetime import datetime

from django.forms.models import modelform_factory
from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import BaseUpdateView, CreateView, UpdateView, DeleteView

from posts.forms import SearchForm, PostBaseForm, PostEditForm, PostCreateForm, PostDeleteForm, CommentFormSet
from posts.models import Post


# Create your views here.

# def index(request: HttpRequest) -> HttpResponse:
#     return HttpResponse("Hello, world. You're at the polls index.")
#
# class IndexView(View):
#     def get(self, request:HttpRequest) -> HttpResponse:
#         print("In class-based view")
#         return HttpResponse("Hello, world.")
#
#     def post(self, request:HttpRequest) -> HttpResponse:
#         ...

class IndexView(TemplateView):
    template_name = 'index.html'
    # extra_context = {
    #     'current_date': datetime.now(),
    # }   - static method, the value is saved in a constant but not updated regularly

    # def get_template_names(self):
    #     if self.request.user.is_staff:
    #         return ['posts/dashboard.html']

    # def get_context_data(self, **kwargs):
    #     kwargs.update({
    #         'current_date': datetime.now(),
    #     })
    #     return kwargs                  # dynamic method, the value is updated and shown dynamically

class MyRedirectView(RedirectView):
    # url = '/dashboard/'    # static way
    pattern_name = 'dashboard'     # 2nd static way

    # def get_redirect_url(self, *args, **kwargs): # dynamic way
    #     ...

def dashboard(request: HttpRequest) -> HttpResponse:
    form = SearchForm(request.GET or None) # load what is inside, if it's not an empty dictionary or return None
    posts = Post.objects.all()

    if request.method == "GET":
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = Post.objects.filter(title__icontains=query)

    context = {'posts':posts, 'form':form}

    #below lines were commented in order to test Forms lecture
    # context = {
    #     'posts':  [
    #         {
    #         'title': 'This is a test post 1',
    #         'content': '',
    #         'author': 'Boris',
    #         'created_at': datetime.datetime.now(),
    #          },
    #         {
    #         'title': 'This is a test post 2',
    #         'content': '*Some* Description here',
    #         'author': 'Pesho',
    #         'created_at': datetime.datetime.now(),
    #         },
    #         {
    #          'title': 'This is a test post 3',
    #         'content': '**Some** <i>Description</i> here',
    #         'author': 'Gosho',
    #         'created_at': datetime.datetime.now(),
    #         },
    #     ],
    # }

    return render(request, 'posts/dashboard.html', context)

class AddPostView(CreateView):
    template_name = 'posts/add-post.html'   # we can skip that if we use the formula for naming
    form_class = PostCreateForm
    success_url = reverse_lazy('dashboard')

# def add_post(request: HttpRequest) -> HttpResponse:
#     form = PostCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             # post = Post(
#             #     title=form.cleaned_data['title'],
#             #     content=form.cleaned_data['content'],
#             #     author=form.cleaned_data['author'],
#             #     language=form.cleaned_data['languages'],
#             # )
#             # post.save()
#             form.save() # only in ModelForm
#
#             return redirect('dashboard')
#
#     context = {'form':form}
#
#     return render(request, 'posts/add-post.html', context)


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')

    def get_form_class(self):
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        if self.request.user.is_staff:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'language', 'image'), widgets=widgets)
        return modelform_factory(Post, fields=('content', 'image'), widgets=widgets)

# def edit_post(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#
#
#     if request.user.is_staff:
#         PostForm = modelform_factory(Post, fields=('title', 'content', 'author', 'language'))
#     else:
#         PostForm = modelform_factory(Post, fields=('content',))
#
#     form = PostForm(
#         data=request.POST or None,
#         instance=post,   # model forms only
#     )
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     context = {'form':form, 'post':post}
#
#     return render(request, 'posts/edit-post.html', context)

class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')
    form_class = PostDeleteForm

    def get_initial(self):
        return self.get_object().__dict__


# def delete_post(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     form = PostDeleteForm(
#         instance=post,
#     )
#
#     if request.method == "POST":
#         post.delete()
#         return redirect('dashboard')
#
#     context = {'form': form, 'post': post}
#
#     return render(request, 'posts/edit-post.html', context)

def details_post(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    formset = CommentFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.pk)

    context = {'post':post, 'formset':formset}

    return render(request, 'posts/posts_details.html', context)





