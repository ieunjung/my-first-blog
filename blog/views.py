from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    #all() #filter(published_date__lte=timezone.now()).order_by('published_date') #filter(title__contains='title')
#request 를 넘겨받아서, 템플릿을 보여준다. 매개변수 posts 이용.
    return render(request, 'blog/post_list.html', { 'posts': posts })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', { 'post':post })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        #유효성 검사
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', { 'form': form })


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
