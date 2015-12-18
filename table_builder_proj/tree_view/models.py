from django.db import models

class TreeNode(models.Model):
    text = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, null=True, blank=True)
    selectedIcon = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=15, null=True, blank=True)
    backColor = models.CharField(max_length=15, null=True, blank=True)
    href = models.CharField(max_length=15, null=True, blank=True)
    selectable = models.NullBooleanField()
    parentNode = models.ForeignKey("TreeNode", null=True, blank=True)

    def __str__(self):
        return self.text
