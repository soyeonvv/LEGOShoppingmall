from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'mypages/homepage.html')

def mypage(request) :
    return render(request, 'mypages/mypage.html')