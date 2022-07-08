from django.shortcuts import render
import csv

def index(request):
    template = 'sales_dashboard/index.html'
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, template, context)

def sales_dashboard(request):    
    template = 'sales_dashboard/sales_dashboard.html'
    title = 'Данные по продажам'

    with open("/home/vasiliy/Dev/dashboards_tdtpl/dashboards/sales_dashboard/data/test.csv", encoding='utf-8') as r_file:
        fieldnames = ['year', 'month_number', 'month', 'sales']
        file_data = csv.DictReader(r_file, delimiter = "|", fieldnames = fieldnames)

        context = {
            'title': title,
            'file_data': file_data,
        }
        return render(request, template, context)