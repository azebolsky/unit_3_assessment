from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>', views.delete, name='delete_widget'),
]