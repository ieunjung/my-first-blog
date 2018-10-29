from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('created_date')
    #all() #filter(published_date__lte=timezone.now()).order_by('published_date') #filter(title__contains='title')
#request 를 넘겨받아서, 템플릿을 보여준다. 매개변수 posts 이용.
    return render(request, 'blog/post_list.html', { 'posts': posts })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
