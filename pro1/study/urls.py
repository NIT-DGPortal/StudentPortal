from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='study-home'),
    path('year_1/year_1_doc/',views.year_1_doc, name='first-year-doc'),
    path('year_1/',views.year_1, name='first-year'),

    path('cs/year_2/',views.cs_second, name='study-cs-second'),
    path('cs/year_3/',views.cs_third, name='study-cs-third'),
    path('cs/year_4/',views.cs_fourth, name='study-cs-fourth'),

    path('ec/year_2/',views.ec_second, name='study-ec-second'),
    path('ec/year_3/',views.ec_third, name='study-ec-third'),
    path('ec/year_4/',views.ec_fourth, name='study-ec-fourth'),

    path('ee/year_2/',views.ee_second, name='study-ee-second'),
    path('ee/year_3/',views.ee_third, name='study-ee-third'),
    path('ee/year_4/',views.ee_fourth, name='study-ee-fourth'),

    path('it/year_2/',views.it_second, name='study-it-second'),
    path('it/year_3/',views.it_third, name='study-it-third'),
    path('it/year_4/',views.it_fourth, name='study-it-fourth'),

    path('bt/year_2/',views.bt_second, name='study-bt-second'),
    path('bt/year_3/',views.bt_third, name='study-bt-third'),
    path('bt/year_4/',views.bt_fourth, name='study-bt-fourth'),

    path('mm/year_2/',views.mm_second, name='study-mm-second'),
    path('mm/year_3/',views.mm_third, name='study-mm-third'),
    path('mm/year_4/',views.mm_fourth, name='study-mm-fourth'),

    path('ch/year_2/',views.ch_second, name='study-ch-second'),
    path('ch/year_3/',views.ch_third, name='study-ch-third'),
    path('ch/year_4/',views.ch_fourth, name='study-ch-fourth'),

    path('ce/year_2/',views.ce_second, name='study-ce-second'),
    path('ce/year_3/',views.ce_third, name='study-ce-third'),
    path('ce/year_4/',views.ce_fourth, name='study-ce-fourth'),

]
