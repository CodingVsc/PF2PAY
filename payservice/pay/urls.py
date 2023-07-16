from django.urls import path
from . import views

urlpatterns = [
    path('create-account/', views.UserCreateApiView.as_view()),
    path('balance-replenishment/', views.BalanceReplenishmentApiView.as_view()),
    path('balance-withdrawal/', views.BalanceWithdrawalApiView.as_view()),
    path('transaction-create/', views.TransactionCreateApiView.as_view()),
    path('user-transfers/<slug:pk>/', views.TransferListApiView.as_view()),
]