from django.db import models
from company.models import Company

class Interview(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    selection_phase = models.CharField(max_length=200, null=True, blank=True)
    selection_date = models.DateTimeField(null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    reflection = models.TextField(null=True, blank=True)
    other = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)