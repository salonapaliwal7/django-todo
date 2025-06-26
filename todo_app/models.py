from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    #  tuples : (stored_value, human_readable_label),
    priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Med', 'Med'), ('Low', 'Low')])
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Done', 'Done')])
