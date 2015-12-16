from django.db import models


# Model for Account Data
class Account(models.Model):

    STATUS_CHOICES = (
        ('Inactive', 'Inactive'),
        ('Active', 'Active'),
    )

    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    status = models.CharField(max_length=8,
                        choices=STATUS_CHOICES,
                        default='Active')

    # Function for readability of Account class instances
    def __str__(self):
        return self.name
