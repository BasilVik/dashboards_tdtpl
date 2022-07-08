from django.urls import path
from . import views

app_name = 'sales_dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('sales_dashboard/', views.sales_dashboard, name='sales_dashboard'),
] 