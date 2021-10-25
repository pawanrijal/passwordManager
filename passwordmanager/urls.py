from django.urls import path

from . import views

urlpatterns = [
    path('home/<str:username>',views.home,name='home'),
    path('addpassword',views.addPassword,name='addpassword'),
    path('',views.homepage,name='homepage')

]