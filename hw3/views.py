# views.py

from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Order, Product

def ordered_products(request):
    # Получаем текущую дату
    current_date = datetime.now().date()

    # Определяем начальную и конечную даты в соответствии с выбранным временным интервалом
    interval = request.GET.get('interval')
    if interval == 'week':
        start_date = current_date - timedelta(days=7)
    elif interval == 'month':
        start_date = current_date - timedelta(days=30)
    elif interval == 'year':
        start_date = current_date - timedelta(days=365)
    else:
        start_date = current_date - timedelta(days=365)  # По умолчанию за год

    # Получаем все заказы клиента за выбранный период
    orders = Order.objects.filter(client=request.user, order_date__gte=start_date)

    # Получаем все товары из этих заказов и убираем повторяющиеся товары
    ordered_products = Product.objects.filter(order__in=orders).distinct()

    context = {
        'ordered_products': ordered_products
    }

    return render(request, 'ordered_products.html', context)
