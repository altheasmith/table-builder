from rest_framework import serializers
from tree_view.models import TreeNode


# Django Rest Framework Serialization of Account Data
class TreeNodeSerializer(serializers.ModelSerializer):
    '''
    Serializer for TreeNode data
    '''
    class Meta:
        model = TreeNode
