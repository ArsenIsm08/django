from django.shortcuts import render
import logging

# Получаем объект логгера
logger = logging.getLogger(__name__)

def index(request):
    # Данные о вашем сайте и о вас
    site_info = "Это мой первый Django-сайт"
    about_me = "Меня зовут Иван и я изучаю Django"

    # HTML-вёрстка для представления главной страницы
    index_html = f"""
    <h1>Добро пожаловать на мой сайт!</h1>
    <p>{site_info}</p>
    """

    # Логируем посещение страницы
    logger.info("Посещена главная страница")

    return render(request, 'index.html', {'html': index_html})

def about(request):
    # HTML-вёрстка для представления "о себе"
    about_html = f"""
    <h2>Обо мне</h2>
    <p>{about_html}</p>
    """

    # Логируем посещение страницы
    logger.info("Посещена страница 'о себе'")

    return render(request, 'about.html', {'html': about_html})