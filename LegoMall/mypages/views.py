from django.shortcuts import render
from shopping.models import Post, Manufacturer, Category, Comment

# Create your views here.
def homepage(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'mypages/homepage.html',
                {'recent_posts' : recent_posts})

def mypage(request) :
    writer = request.user
    comments = Comment.objects.filter(author=writer).order_by('-created_at')
    return render(request, 'mypages/mypage.html', context={'comments':comments})

def manufacturer(request) :
    manufacturers = Manufacturer.objects.all()
    categories = Category.objects.all()
    no_category_post_count = Post.objects.filter(category=None).count()
    return render(request, 'mypages/company.html', {'manufacturers' : manufacturers, 'categories' : categories, 'no_category_post_count' : no_category_post_count})