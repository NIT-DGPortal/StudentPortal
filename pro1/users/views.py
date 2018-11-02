from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':   ## data sent do further things ie validation checks
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created. Log In to continue!')
			return redirect('blog-home')

	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})
	## get get
	## post check validation


## messages.debug/info/success/warning/error
#  UserRegisterForm replacing UserCreationForm
# crispy-form makes it look awesome

@login_required
def profile(request):
	return render(request,'users/profile.html')
