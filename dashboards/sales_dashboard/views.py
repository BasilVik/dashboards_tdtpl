from django.shortcuts import render


# Главная страница
def sales_dashboard(request):    
    template = 'sales_dashboard/index.html'
    title = 'Данные по продажам'
    text = 'Текст страницы'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)