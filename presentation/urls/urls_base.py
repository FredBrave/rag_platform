from django.contrib import admin
from django.urls import path, include
from presentation.views import usuario_views, page_views

urlpatterns = [
    path("register/", usuario_views.registerPage, name="register"),
    path('login/', usuario_views.loginPage, name='login'),
    path('logout/', usuario_views.logoutUser, name='logout'),
    path('', page_views.home, name='home'),
    path('mis_rags/', page_views.mis_rags, name='mis_rags'),
]