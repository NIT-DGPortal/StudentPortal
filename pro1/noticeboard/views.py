from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(redirect_field_name='')
def home(request):
	return render(request,'noticeboard/home.html')
    #return HttpResponse('<p> Hello </p>')
