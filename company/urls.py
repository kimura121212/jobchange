from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
]