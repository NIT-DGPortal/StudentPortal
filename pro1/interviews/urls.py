from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='interview-home'),
    path('internship/<int:internship_id>/',
         views.internship, name='internship'),
    path('placement/<int:placement_id>/', views.placement, name='placement'),
]
