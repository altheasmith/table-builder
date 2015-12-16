from django.db import models

class Account(models.Model):
    STATUS_CHOICES = (
        ('inactive', 'Inactive'),
        ('active', 'Active'),
    )
    name = CharField(max_length=30)
    amount = IntegerField()
    status = CharField(max_length=8,
                        choices=STATUS_CHOICES,
                        default='active')
