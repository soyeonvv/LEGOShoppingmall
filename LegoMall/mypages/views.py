from django.shortcuts import render
from shopping.models import Post, Manufacturer, Category

# Create your views here.
def homepage(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'mypages/homepage.html',
                {'recent_posts' : recent_posts})

def mypage(request) :
    return render(request, 'mypages/mypage.html')

def manufacturer(request) :
    manufacturers = Manufacturer.objects.all()
    categories = Category.objects.all()
    no_category_post_count = Post.objects.filter(category=None).count()
    return render(request, 'mypages/company.html', {'manufacturers' : manufacturers, 'categories' : categories, 'no_category_post_count' : no_category_post_count})