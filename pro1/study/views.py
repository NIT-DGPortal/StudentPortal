from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(redirect_field_name='')
def home(request):
	return render(request,'study/home.html')
    #return HttpResponse('<p> Hello </p>')

@login_required(redirect_field_name='')
def cs(request):
	return render(request,'study/cs.html')

@login_required(redirect_field_name='')
def ec(request):
	return render(request,'study/ec.html')

@login_required(redirect_field_name='')
def ee(request):
	return render(request,'study/ee.html')

@login_required(redirect_field_name='')
def mm(request):
	return render(request,'study/mm.html')

@login_required(redirect_field_name='')
def bt(request):
	return render(request,'study/bt.html')

@login_required(redirect_field_name='')
def it(request):
	return render(request,'study/it.html')

@login_required(redirect_field_name='')
def ce(request):
	return render(request,'study/ce.html')

@login_required(redirect_field_name='')
def ch(request):
	return render(request,'study/ch.html')
