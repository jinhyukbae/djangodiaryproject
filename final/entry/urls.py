from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.entry, name='entry'),
    path('show', views.show, name='show'),
    path('show/<int:diary_id>', views.detail, name='detail'),
    path('productivity/', views.productivity, name='productivity'),
    path('login/', auth_views.LoginView.as_view(template_name='entry/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]