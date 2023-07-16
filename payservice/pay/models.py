from django.db import models


class UserAccount(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    user_id = models.UUIDField()


class Balance(models.Model):
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    operation_type = models.CharField(max_length=50)
    is_accept = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    acc_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='balances')


class TransferHistory(models.Model):
    acc_from = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='transfers_from')
    acc_to = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='transfers_to')
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    operation_type = models.CharField(max_length=50)
    is_frozen = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    acc_from = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='transactions_from')
    acc_to = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='transactions_to')
    product_id = models.IntegerField()
