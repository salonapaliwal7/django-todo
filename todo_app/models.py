from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    #  tuples : (stored_value, human_readable_label),
    priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Med', 'Med'), ('Low', 'Low')])
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Done', 'Done')])
    created_at = models.DateTimeField(auto_now_add=True)