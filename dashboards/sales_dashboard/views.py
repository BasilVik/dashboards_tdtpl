from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница дашборда Продажи
def sales_dashboard(request):
    return HttpResponse('Данные по продажам')