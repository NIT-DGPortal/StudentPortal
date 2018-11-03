from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile

def register(request):
	if request.method == 'POST':   ## data sent do further things ie validation checks
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			#user.Profile.email_confirmed = False
			user.save()
			#player, created = UserProfile.objects.get_or_create(user=request.user)
			#user.profile = User.objects.create(user=request.user)
			current_site = get_current_site(request)
			subject = 'Activate your account!'
			message = render_to_string('users/activation.html', {
				'user' : user,
				'domain' : current_site,
				'uid' : urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token' : account_activation_token.make_token(user),
			})
			#user.email_user(subject, message)
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
			return redirect('mail_sent')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})
	## get get
	## post check validation

def mail_sent(request):
	return render(request, 'users/mail_sent.html')

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		#print(uid)
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.profile.email_confirmed = True
		user.save()
		login(request, user)
		return redirect('profile')
	
	else:
		return render(request, 'users/invalid_registration.html')
	
## messages.debug/info/success/warning/error
# UserRegisterForm replacing UserCreationForm
# crispy-form makes it look awesome

@login_required
def profile(request):
	return render(request,'users/profile.html')
