from django.db.models import F
from rest_framework import generics
from rest_framework.response import Response

import requests

from .serializers import (UserSerializer, BalanceSerializer,
                          TransactionSerializer, TransferSerializer)
from .models import UserAccount, Transaction, TransferHistory


class UserCreateApiView(generics.CreateAPIView):
    serializer_class = UserSerializer


class BalanceReplenishmentApiView(generics.CreateAPIView):
    serializer_class = BalanceSerializer

    def perform_create(self, serializer):
        serializer.save()
        acc_id = serializer.instance.acc_id
        amount = serializer.instance.sum
        UserAccount.objects.filter(id=acc_id).update(balance=F('balance') + amount)


class BalanceWithdrawalApiView(generics.CreateAPIView):
    serializer_class = BalanceSerializer

    def perform_create(self, serializer):
        serializer.save()
        acc_id = serializer.instance.acc_id
        amount = serializer.instance.sum
        user_obj = UserAccount.objects.get(id=acc_id)
        balance = user_obj.balance
        if amount <= balance:
            UserAccount.objects.filter(id=acc_id).update(balance=F('balance') - amount)
        else:
            return Response({'error': 'Failed to create transaction'})


class TransactionCreateApiView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save()
        transaction_id = serializer.instance.id
        product_id = serializer.instance.product_id
        acc_from = serializer.instance.acc_from
        acc_to = serializer.instance.acc_to

        product_data = requests.get(f'http://127.0.0.1:8000/api/v1/product-detail/{product_id}/')

        if product_data.status_code == 200:
            product_dict = product_data.json()
            price = product_dict.get('price')

            # Дальнейшая логика (меняем is_active для скрытия продукта с ленты)
            Transaction.objects.filter(id=transaction_id).update(is_accepted=True)
            data = {'is_active': False}
            requests.patch(f'http://127.0.0.1:8000/api/v1/product-detail/{product_id}/', data)

            # Проверка баланса и вычет средств
            acc_from_obj = UserAccount.objects.get(id=acc_from)
            if acc_from_obj.balance >= price:
                UserAccount.objects.filter(id=acc_from).update(balance=F('balance') - price)
                UserAccount.objects.filter(id=acc_to).update(balance=F('balance') + price)
                TransferHistory.objects.create(acc_from=acc_from, acc_to=acc_to, sum=price)
            else:
                Response({'error': 'Failed to create transaction, your balance less than price'})
        else:
            return Response({'error': 'Failed to create transaction'})


class TransferListApiView(generics.ListAPIView):
    serializer_class = TransferSerializer

    def get_queryset(self):
        acc_id = self.kwargs['pk']
        user_obj_1 = UserAccount.objects.filter(acc_from=acc_id)
        user_obj_2 = UserAccount.objects.filter(acc_to=acc_id)
        combined_queryset = user_obj_1 | user_obj_2
        return combined_queryset





