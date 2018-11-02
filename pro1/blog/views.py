from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.



posts = [  # list of dictionaries
	{
		'author' : 'MonsijBiswal',
		'title' : 'Initial Post',
		'content' : 'The first notice',
		'date_posted' : 'October 29, 2018'
	},

	{
		'author' : 'MonsijBiswal',
		'title' : 'Second Post',
		'content' : 'An important notice',
		'date_posted' : 'October 30, 2018'
	},
]

context = {
		'posts' : posts
}
@login_required(redirect_field_name='')
def home(request):
	return render(request,'blog/home.html',context)


def about(request):
	return render(request,'blog/about.html',context)
