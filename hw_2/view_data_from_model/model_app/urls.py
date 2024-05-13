from django.urls import path

from .views import view_articles

urlpatterns = [
    path('', view_articles)
]