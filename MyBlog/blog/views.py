from django.shortcuts import render
from .models import Post
posts = [
	{
		'authors': 'AleksandarBukvic',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'August 27,2018'
	},

	{
		'authors':'Jane Dough',
		'title': 'Blog Post 2',
		'content':'Second Blog Content',
		'date_posted': 'August 28, 2019'
	}
]

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)
# Create your views here.
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
