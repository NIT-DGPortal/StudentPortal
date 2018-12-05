from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required(redirect_field_name='')
def home(request):
	return render(request,'blog/home.html')

def contact(request):
	return render(request,'blog/contact.html')

def about(request):
	return render(request,'blog/about.html')

def contributor(request):
	return render(request, 'blog/contributor.html')
