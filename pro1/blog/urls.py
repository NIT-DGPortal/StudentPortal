from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
	#path('', views.home, name='blog-home'),
	path('about/',views.about, name='blog-about'),
	path('home/', views.home, name='blog-home'),
	path('noticeboard/', include('noticeboard.urls')),
	path('study/',include('study.urls')),
]
