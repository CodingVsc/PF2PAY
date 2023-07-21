from django.db.models import F, Q
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import (UserSerializer, BalanceSerializer,
                          TransactionSerializer, TransferSerializer)
from .models import UserAccount, TransferHistory
from .service import transaction_logic


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
            return Response({'error': 'Failed to create transaction'}, status=status.HTTP_400_BAD_REQUEST)


class TransactionCreateApiView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save()
        transaction_id = serializer.instance.id
        product_id = serializer.instance.product_id
        acc_from = serializer.instance.acc_from
        acc_to = serializer.instance.acc_to

        result = transaction_logic(product_id, transaction_id, acc_from, acc_to)

        if 'success' in result:
            return Response({'status': 'Transaction created successfully'})
        elif 'error' in result:
            return Response({'error': result['error']}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Failed to create transaction'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TransferListApiView(generics.ListAPIView):
    serializer_class = TransferSerializer

    def get_queryset(self):
        acc_id = self.kwargs['pk']
        queryset = TransferHistory.objects.filter(Q(acc_from=acc_id) | Q(acc_to=acc_id))
        return queryset





