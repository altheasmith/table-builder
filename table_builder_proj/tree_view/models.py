from django.db import models

class TreeNode(models.Model):
    text = models.CharField(max_length=50)
    parentNode = models.ForeignKey("TreeNode", null=True, blank=True)

    def __str__(self):
        return self.text
