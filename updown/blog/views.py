from django.shortcuts import render
from .models import Post

posts = [
	{
		'author': 'User1',
		'title': 'Post 2',
		'content': 'Post 2',
		'date_posted': '13-04-13'
	},
	{
		'author': 'User2',
		'title': 'Post 1',
		'content': 'Post 1',
		'date_posted': '14-04-14'
	}
]


def home(request):
    context = {
		'posts': Post.objects.all()
	}
    return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
