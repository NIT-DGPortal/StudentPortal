from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='study-home'),
    path('cs/',views.cs, name='study-cs'),
    path('ec/',views.ec, name='study-ec'),
    path('ee/',views.ee, name='study-ee'),
    path('mm/',views.mm, name='study-mm'),
    path('bt/',views.bt, name='study-bt'),
    path('ch/',views.ch, name='study-ch'),
    path('ce/',views.ce, name='study-ce'),

]
