from rest_framework import serializers

from .models import UserAccount, Balance, Transaction


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ('user_id',)


class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Balance
        fields = ('sum', 'operation_type', 'is_accept', 'acc_id')


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('operation_type', 'acc_from', 'acc_to', 'product_id')


