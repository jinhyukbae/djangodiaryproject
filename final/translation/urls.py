from django.urls import path
from . import views

urlpatterns = [
    path('translate/', views.translate_app, name='trans'),
]
