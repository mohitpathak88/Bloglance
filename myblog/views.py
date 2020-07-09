from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Mohit Pathak',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 29, 2020' 
    },
    {
        'author': 'Harshit Pathak',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 30, 2020' 
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'myblog/home.html', context)

def about(request):
    return render(request, 'myblog/about.html', {'title': 'About'})

