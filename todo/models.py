from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    priority_choices = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    priority = models.CharField(max_length=10, choices=priority_choices, default='MEDIUM')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title