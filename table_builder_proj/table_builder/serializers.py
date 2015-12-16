from rest_framework import serializers
from table_builder.models import Account


class AccountSerializer(serializers.ModelSerializer):
    '''
    Serializer for Account data
    '''
    class Meta:
        model = Account
        fields = ('name','amount','status')
