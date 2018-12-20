from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='year1-home'),
    path('year_1_doc/',views.year_1_doc, name='first-year-doc'),
    
    ]