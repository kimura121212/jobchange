from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.CompanyTop.as_view(), name='top'),
    path('register', views.CompanyRegister.as_view(), name='register'),
    path('register_complete', views.CompanyRegisterComplete.as_view(), name='register_complete'),
    path('update/<int:pk>', views.CompanyUpdate.as_view(), name='update'),
    path('update_complete', views.CompanyUpdateComplete.as_view(), name='update_complete'),
    # path('delete/<int:pk>', views.CompanyDelete.as_view(), name='delete'),
]