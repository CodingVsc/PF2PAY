import pytest
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_authenticated_endpoint(api_client, user_account):
    url = reverse('pay:user_transfers', args=(user_account.id,))
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


