from django.urls import path
from . import views

app_name = 'sales_dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('sales_dashboard/', views.sales_dashboard, name='sales_dashboard'),
    path('sales_astor_dashboard/', views.sales_astor_dashboard, name='sales_astor_dashboard'),
    path('bank_dashboard/', views.bank_dashboard, name='bank_dashboard'),
    path('account_total_dashboard/', views.account_total_dashboard, name='account_total_dashboard'),
    path('account_dashboard/', views.account_dashboard, name='account_dashboard'),
] 