from django.db import models

class TreeNode(models.Model):
    text = models.CharField(max_length=50)
    parentNode = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
