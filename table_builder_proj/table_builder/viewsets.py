from rest_framework import viewsets
from table_builder.models import Account
from table_builder.serializers import AccountSerializer


# Account Viewset for Django Rest Framework API
class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows account data to be queried
    """
    queryset = Account.objects.all().order_by('name')
    serializer_class = AccountSerializer
