from django.urls import path 
from . import views

urlpatterns = [
    path('',views.pages),
    path ('misruni', views.home),
    path ('login.must',views.log),
    path('stuprofile',views.stuprofile),
    path('confirm',views.ensure),
    path('certificate/',views.certificate),

]