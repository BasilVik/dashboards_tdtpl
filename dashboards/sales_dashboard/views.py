from django.shortcuts import render
import csv

def index(request):
    template = 'sales_dashboard/index.html'
    title = 'Аналитика'
    context = {
        'title': title,
    }
    return render(request, template, context)

def sales_dashboard(request):    
    template = 'sales_dashboard/sales_dashboard.html'
    title = 'Данные по продажам'

    with open("/home/vasiliy/Dev/dashboards_tdtpl/dashboards/sales_dashboard/data/sales.csv", encoding='utf-8') as r_file:
        fieldnames = ['year', 'month_number', 'month', 'sales']
        file_data = csv.DictReader(r_file, delimiter = "|", fieldnames = fieldnames)

        context = {
            'title': title,
            'file_data': file_data,
        }
        return render(request, template, context)

def sales_astor_dashboard(request):    
    template = 'sales_dashboard/sales_dashboard.html'
    title = 'Данные по продажам Астор'

    with open("/home/vasiliy/Dev/dashboards_tdtpl/dashboards/sales_dashboard/data/sales_astor.csv", encoding='utf-8') as r_file:
        fieldnames = ['year', 'month_number', 'month', 'sales']
        file_data = csv.DictReader(r_file, delimiter = "|", fieldnames = fieldnames)

        context = {
            'title': title,
            'file_data': file_data,
        }
        return render(request, template, context)

def bank_dashboard(request):
    template = 'sales_dashboard/bank_dashboard.html'
    title = 'Данные по счетам'

    with open("/home/vasiliy/Dev/dashboards_tdtpl/dashboards/sales_dashboard/data/bank.csv", encoding='utf-8') as r_file:
        fieldnames = ['organization', 'bank', 'amount']
        file_data = csv.DictReader(r_file, delimiter = "|", fieldnames = fieldnames)

        context = {
            'title': title,
            'file_data': file_data,
        }
        return render(request, template, context)

def account_total_dashboard(request):
    template = 'sales_dashboard/account_total_dashboard.html'
    title = 'Данные по взаиморасчетам общие'

    with open("/home/vasiliy/Dev/dashboards_tdtpl/dashboards/sales_dashboard/data/acc_total.csv", encoding='utf-8') as r_file:
        fieldnames = ['enterprise_debt', 'partner_debt']
        file_data = csv.DictReader(r_file, delimiter = "|", fieldnames = fieldnames)

        context = {
            'title': title,
            'file_data': file_data,
        }
        return render(request, template, context)

def account_dashboard(request):
    template = 'sales_dashboard/account_dashboard.html'
    title = 'Данные по взаиморасчетам'

    with open("/home/vasiliy/Dev/dashboards_tdtpl/dashboards/sales_dashboard/data/acc.csv", encoding='utf-8') as r_file:
        fieldnames = ['partner', 'enterprise_debt', 'partner_debt']
        file_data = csv.DictReader(r_file, delimiter = "|", fieldnames = fieldnames)

        context = {
            'title': title,
            'file_data': file_data,
        }
        return render(request, template, context)