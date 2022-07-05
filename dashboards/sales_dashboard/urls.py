from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница дашборда Продажи
    path('sales_dashboard/', views.sales_dashboard),
] 