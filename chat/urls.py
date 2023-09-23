from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import path
from . import views

def custom_logout(request):
    logout(request)
    # Redirect to the desired page after logout, e.g., 'index'
    return redirect('index')

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    path('logout/', custom_logout, name='logout'),
    path('register/', views.register_view, name='register'),
]
