from django.db import models

# Create your models here.


class UserAccount(models.Model):
    balance = models.FloatField(default=0)
    user_id = models.UUIDField()


class Balance(models.Model):
    sum = models.FloatField(default=0)
    operation_type = models.CharField(max_length=50)
    is_accept = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    acc_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)


class TransferHistory(models.Model):
    acc_from = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    acc_to = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    sum = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    is_frozen = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    acc_from = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    acc_to = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    product_id = models.IntegerField()


class TransactionHistory(models.Model):
    operation_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)