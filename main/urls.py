from django.contrib.auth.views import LoginView
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('register/', views.register, name='register', ),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('booklist/' , BookListAPIView.as_view(), name='booklist'),
    path('bookdetail/<int:pk>/', BookDetailAPIView.as_view(), name='bookdetail'),
    path('about/', AboutAPIView.as_view(), name='about'),
    path('orderlist/', OrderListAPIView.as_view(), name='orderlist'),
    path('orderdetail/<int:pk>/', OrderDetailAPIView.as_view(), name='orderdetail'),
    path('categorylist/', CategoryListAPIView.as_view(), name='categorylist'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
]
