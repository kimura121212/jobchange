from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.CompanyTop.as_view(), name='top'),
    path('register', views.CompanyRegister.as_view(), name='register'),
    path('register_complete', views.CompanyRegisterComplete.as_view(), name='register_complete'),
]