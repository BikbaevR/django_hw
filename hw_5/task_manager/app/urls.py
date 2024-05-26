
from django.urls import path
from .views import index, done, un_done,delete

urlpatterns = [
    path('', index, name='index'),
    path('done/<int:task_id>', done, name='done'),
    path('un_done/<int:task_id>', un_done, name='un_done'),
    path('delete/<int:task_id>', delete, name='delete')

]