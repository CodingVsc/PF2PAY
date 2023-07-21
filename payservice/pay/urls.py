from django.urls import path
from . import views


app_name = 'pay'

urlpatterns = [
    path('create-account/', views.UserCreateApiView.as_view(), name='create_account'),
    path('balance-replenishment/', views.BalanceReplenishmentApiView.as_view(), name='balance_replenishment'),
    path('balance-withdrawal/', views.BalanceWithdrawalApiView.as_view(), name='balance_withdrawal'),
    path('transaction-create/', views.TransactionCreateApiView.as_view(), name='transaction_create'),
    path('user-transfers/<slug:pk>/', views.TransferListApiView.as_view(), name='user_transfers'),
]