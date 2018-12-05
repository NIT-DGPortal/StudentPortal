from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
	#path('', views.home, name='blog-home'),
	path('about/',views.about, name='blog-about'),
	path('home/', views.home, name='blog-home'),
	path('contact/',views.contact, name='blog-contact'),
	path('contributors/', views.contributor, name='blog-contributor'),
	path('noticeboard/', include('noticeboard.urls')),
	path('study/',include('study.urls')),
	path('interviews/',include('interviews.urls')),
]
