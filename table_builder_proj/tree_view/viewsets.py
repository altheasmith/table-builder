from rest_framework import viewsets
from tree_view.models import TreeNode
from tree_view.serializers import TreeNodeSerializer


# TreeNode Viewset for Django Rest Framework API
class TreeNodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tree node data to be queried
    """
    queryset = TreeNode.objects.all()
    serializer_class = TreeNodeSerializer
