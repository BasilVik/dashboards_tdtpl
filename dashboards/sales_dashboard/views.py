from django.shortcuts import render


# Главная страница
def index(request):    
    template = 'sales_dashboard/index.html'
    title = 'Главная страница'
    context = {
        'title': title,
        'text': 'Главная страница',
    }
    return render(request, template, context)