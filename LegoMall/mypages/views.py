from django.shortcuts import render
from shopping.models import Post

# Create your views here.
def homepage(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'mypages/homepage.html',
                {'recent_posts' : recent_posts})

def mypage(request) :
    return render(request, 'mypages/mypage.html')