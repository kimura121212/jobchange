from django.urls import path
from . import views

app_name = 'interview'

urlpatterns = [
    path('<int:pk>', views.InterviewTop.as_view(), name='top'),
    path('register/<int:pk>', views.InterviewRegister.as_view(), name='register'),
    path('register_complete', views.InterviewRegisterComplete.as_view(), name='register_complete'),
    path('update/<int:pk>', views.InterviewUpdate.as_view(), name='update'),
    path('update_complete', views.InterviewUpdateComplete.as_view(), name='update_complete'),
    path('delete/<int:pk>', views.InterviewDelete.as_view(), name='delete'),
]