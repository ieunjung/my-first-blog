from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(title__contains='title') #all() #filter(published_date__lte=timezone.now()).order_by('published_date')
#request 를 넘겨받아서, 템플릿을 보여준다. 매개변수 posts 이용.
    return render(request, 'blog/post_list.html', {'posts':posts})
