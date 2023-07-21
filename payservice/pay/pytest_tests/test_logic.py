import uuid

import pytest
from _decimal import Decimal
from rest_framework import status
from rest_framework.reverse import reverse

from pay.models import UserAccount, TransferHistory


@pytest.mark.django_db
def test_create_user_account(api_client):
    url = reverse('pay:create_account')
    data = {
        'balance': 100.0,
        'user_id': uuid.uuid4()
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert UserAccount.objects.count() == 1
    assert UserAccount.objects.get().user_id == data['user_id']


@pytest.mark.django_db
def test_balance_replenishment(api_client, user_account, form_data_replenishment):
    url = reverse('pay:balance_replenishment')
    response = api_client.post(url, data=form_data_replenishment)
    assert response.status_code == status.HTTP_201_CREATED
    user_account.refresh_from_db()
    assert user_account.balance == Decimal('125.00')


@pytest.mark.django_db
def test_balance_withdrawal(api_client, user_account, form_data_withdrawal):
    url = reverse('pay:balance_withdrawal')
    response = api_client.post(url, data=form_data_withdrawal)
    assert response.status_code == status.HTTP_201_CREATED
    user_account.refresh_from_db()
    assert user_account.balance == 50.0


@pytest.mark.django_db
def test_transaction_create(api_client, user_account, user_account_2):
    url = reverse('pay:transaction_create')
    data = {
        'product_id': 1,
        'acc_from': user_account.id,
        'acc_to': user_account_2.id,
        'sum': 25.0
    }
    response = api_client.post(url, data=data)
    assert response.status_code == status.HTTP_200_OK
    user_account.refresh_from_db()
    user_account_2.refresh_from_db()
    assert user_account.balance == 75.0
    assert user_account_2.balance == 75.0


@pytest.mark.django_db
def test_user_transfers(api_client, user_account, user_account_2):
    TransferHistory.objects.create(acc_from=user_account, acc_to=user_account_2, sum=25.0)
    TransferHistory.objects.create(acc_from=user_account_2, acc_to=user_account, sum=15.0)
    url = reverse('pay:user_transfers', kwargs={'pk': user_account.id})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['sum'] == '25.00'
    assert response.data[1]['sum'] == '15.00'