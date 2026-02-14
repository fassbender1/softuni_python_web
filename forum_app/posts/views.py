from django.forms.models import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from posts.forms import SearchForm, PostBaseForm, PostEditForm, PostCreateForm, PostDeleteForm, CommentFormSet
from posts.models import Post


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")

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

def add_post(request: HttpRequest) -> HttpResponse:
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            # post = Post(
            #     title=form.cleaned_data['title'],
            #     content=form.cleaned_data['content'],
            #     author=form.cleaned_data['author'],
            #     language=form.cleaned_data['languages'],
            # )
            # post.save()
            form.save() # only in ModelForm

            return redirect('dashboard')

    context = {'form':form}

    return render(request, 'posts/add-post.html', context)


def edit_post(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)


    if request.user.is_staff:
        PostForm = modelform_factory(Post, fields=('title', 'content', 'author', 'language'))
    else:
        PostForm = modelform_factory(Post, fields=('content',))

    form = PostForm(
        data=request.POST or None,
        instance=post,   # model forms only
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form':form, 'post':post}

    return render(request, 'posts/edit-post.html', context)


def delete_post(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    form = PostDeleteForm(
        instance=post,
    )

    if request.method == "POST":
        post.delete()
        return redirect('dashboard')

    context = {'form': form, 'post': post}

    return render(request, 'posts/edit-post.html', context)

def details_post(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    formset = CommentFormSet(request.POST or None)

    if request.POST == "POST":
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.pk)

    context = {'post':post, 'formset':formset}

    return render(request, 'posts/posts_details.html', context)





