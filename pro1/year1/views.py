from django.shortcuts import render


def home(request):
	return render(request,'year1/home.html')


def year_1_doc(request):
	return render(request,'year1/year_1_doc.html')

