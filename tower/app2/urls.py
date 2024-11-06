from django.urls import path
from . import views  # Ensure you're importing views properly

urlpatterns = [
    path('', views.home, name='home'),  # Ensure you have a valid view  
    path('blank_page/', views.blank_page, name='blank_page'),
    path('v1/', views.v1, name='v1'),
    path('v2/', views.v2, name='v2'),
    path('v3/', views.v3, name='v3'),
    path('v4/', views.v4, name='v4'),
    path('v5/', views.v5, name='v5'),
    path('v6/', views.v6, name='v6'),
    path('v7/', views.v7, name='v7'),
    path('v8/', views.v8, name='v8'),
    path('tab1/', views.tab1, name='tab1'),
    path('tab2/', views.tab2, name='tab2'),
    path('tab3/', views.tab3, name='tab3'),
    path('tab4/', views.tab4, name='tab4'),
    path('tab5/', views.tab5, name='tab5'),
    path('tab6/', views.tab6, name='tab6'),
    path('c1/', views.c1, name='c1'),
    path('c2/', views.c2, name='c2'),
    path('c3/', views.c3, name='c3'),
    path('c4/', views.c4, name='c4'),
    path('c5/', views.c5, name='c5'),
    path('a1/',views.a1, name='a1'),
    path('a2/',views.a2, name='a2'),
    path('a3/',views.a3, name='a3'),
    path('a4/',views.a4, name='a4'),
    path('a5/',views.a5, name='a5'),

    

]