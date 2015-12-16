from django.db import models

class Account(models.Model):

    STATUS_CHOICES = (
        ('inactive', 'Inactive'),
        ('active', 'Active'),
    )

    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    status = models.CharField(max_length=8,
                        choices=STATUS_CHOICES,
                        default='active')

    def __str__(self):
        return self.name
