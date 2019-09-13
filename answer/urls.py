from django.urls import path
from . import views

app_name = 'answer'

urlpatterns = [
    path('', views.AnswerTop.as_view(), name='top'),
    path('register', views.AnswerRegister.as_view(), name='register'),
    path('register_complete', views.AnswerRegisterComplete.as_view(), name='register_complete'),
    path('update/<int:pk>', views.AnswerUpdate.as_view(), name='update'),
    path('update_complete', views.AnswerUpdateComplete.as_view(), name='update_complete'),
    path('delete/<int:pk>', views.AnswerDelete.as_view(), name='delete'),
]