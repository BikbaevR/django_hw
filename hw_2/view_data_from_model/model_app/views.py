from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import Article


def view_articles(request):
    articles = Article.objects.all()
    #надо было сделать формирование html в контроллере, но так как мы прошли статические файлы - я решил сделать через
    # них, если нужно я переделаю

    return render(request, 'articles/index.html', context={'articles': articles})
