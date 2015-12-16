from rest_framework import serializers
from table_builder.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('name','amount','status')
