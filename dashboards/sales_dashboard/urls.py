from django.urls import path
from . import views

app_name = 'sales_dashboard'

urlpatterns = [
    # Главная страница
    path('sales_dashboard/', views.sales_dashboard, name='sales_dashboard'),
] 