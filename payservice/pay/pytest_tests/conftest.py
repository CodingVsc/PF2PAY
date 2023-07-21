import os
import uuid
import pytest
from django.conf import settings
from rest_framework.test import APIClient

from pay.models import UserAccount


@pytest.fixture
def user_account():
    user = UserAccount.objects.create(
        user_id=uuid.uuid4(),
        balance=100.0
    )
    return user


@pytest.fixture
def user_account_2():
    user = UserAccount.objects.create(
        user_id=uuid.uuid4(),
        balance=50.0
    )
    return user


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def form_data_replenishment(user_account):
    return {
        'sum': 25.0,
        'operation_type': 'replenishment',
        'is_accept': True,
        'acc_id': user_account,
    }


@pytest.fixture
def form_data_withdrawal(user_account):
    return {
        'sum': 50.0,
        'operation_type': 'withdrawal',
        'is_accept': True,
        'acc_id': user_account,
    }

