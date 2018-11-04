from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(redirect_field_name='')
def home(request):
	return render(request,'study/home.html')
    #return HttpResponse('<p> Hello </p>')

@login_required(redirect_field_name='')
def year_1_doc(request):
	return render(request,'study/year_1/year_1_doc.html')

@login_required(redirect_field_name='')
def year_1(request):
	return render(request,'study/year_1/year_1.html')




@login_required(redirect_field_name='')
def cs_second(request):
	return render(request,'study/cs/cs_second.html')

@login_required(redirect_field_name='')
def cs_third(request):
	return render(request,'study/cs/cs_third.html')

@login_required(redirect_field_name='')
def cs_fourth(request):
	return render(request,'study/cs/cs_fourth.html')

@login_required(redirect_field_name='')
def cs(request):
	return render(request,'study/cs/cs.html')




@login_required(redirect_field_name='')
def ec_second(request):
	return render(request,'study/ec/ec_second.html')

@login_required(redirect_field_name='')
def ec_third(request):
	return render(request,'study/ec/ec_third.html')

@login_required(redirect_field_name='')
def ec_fourth(request):
	return render(request,'study/ec/ec_fourth.html')

@login_required(redirect_field_name='')
def ec(request):
	return render(request,'study/ec/ec.html')




@login_required(redirect_field_name='')
def ee_second(request):
	return render(request,'study/ee/ee_second.html')

@login_required(redirect_field_name='')
def ee_third(request):
	return render(request,'study/ee/ee_third.html')

@login_required(redirect_field_name='')
def ee_fourth(request):
	return render(request,'study/ee/ee_fourth.html')

@login_required(redirect_field_name='')
def ee(request):
	return render(request,'study/ee/ee.html')




@login_required(redirect_field_name='')
def mm_second(request):
	return render(request,'study/mm/mm_second.html')

@login_required(redirect_field_name='')
def mm_third(request):
	return render(request,'study/mm/mm_third.html')

@login_required(redirect_field_name='')
def mm_fourth(request):
	return render(request,'study/mm/mm_fourth.html')

@login_required(redirect_field_name='')
def mm(request):
	return render(request,'study/mm/mm.html')




@login_required(redirect_field_name='')
def bt_second(request):
	return render(request,'study/bt/bt_second.html')

@login_required(redirect_field_name='')
def bt_third(request):
	return render(request,'study/bt/bt_third.html')

@login_required(redirect_field_name='')
def bt_fourth(request):
	return render(request,'study/bt/bt_fourth.html')

@login_required(redirect_field_name='')
def bt(request):
	return render(request,'study/bt/bt.html')




@login_required(redirect_field_name='')
def it_second(request):
	return render(request,'study/it/it_second.html')

@login_required(redirect_field_name='')
def it_third(request):
	return render(request,'study/it/it_third.html')

@login_required(redirect_field_name='')
def it_fourth(request):
	return render(request,'study/it/it_fourth.html')

@login_required(redirect_field_name='')
def it(request):
	return render(request,'study/it/it.html')




@login_required(redirect_field_name='')
def ce_second(request):
	return render(request,'study/ce/ce_second.html')

@login_required(redirect_field_name='')
def ce_third(request):
	return render(request,'study/ce/ce_third.html')

@login_required(redirect_field_name='')
def ce_fourth(request):
	return render(request,'study/ce/ce_fourth.html')

@login_required(redirect_field_name='')
def ce(request):
	return render(request,'study/ce/ce.html')




@login_required(redirect_field_name='')
def ch_second(request):
	return render(request,'study/ch/ch_second.html')

@login_required(redirect_field_name='')
def ch_third(request):
	return render(request,'study/ch/ch_third.html')

@login_required(redirect_field_name='')
def ch_fourth(request):
	return render(request,'study/ch/ch_fourth.html')

@login_required(redirect_field_name='')
def ch(request):
	return render(request,'study/ch/ch.html')
