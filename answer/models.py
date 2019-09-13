from django.db import models
from register.models import User

class Answer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)