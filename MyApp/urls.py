from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register,name='register'),
    path('login/',views.login,name='login'),
    path('', views.home,name='home'),

]
