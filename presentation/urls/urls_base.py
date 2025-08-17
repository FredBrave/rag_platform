from django.contrib import admin
from django.urls import path, include
from presentation.views import usuario_views, page_views

urlpatterns = [
    path("register/", usuario_views.registerPage, name="register"),
    path('login/', usuario_views.loginPage, name='login'),
    path('logout/', usuario_views.logoutUser, name='logout'),
    path('', page_views.home, name='home'),
    path('mis_rags/', page_views.mis_rags, name='mis_rags'),
    path('crear_rag/', page_views.crear_rag, name='crear_rag'),
    path('rags/editar/<int:rag_id>/', page_views.editar_rag, name='editar_rag'),
    path('eliminar_rag/<int:rag_id>/', page_views.eliminar_rag, name='eliminar_rag'),
]