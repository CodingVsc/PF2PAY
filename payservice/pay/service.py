import requests

from django.db.models import F

import os

from .models import Transaction, UserAccount, TransferHistory


def transaction_logic(product_id, transaction_id, acc_from, acc_to):

    product_detail_url = os.environ.get('PRODUCT_DETAIL_API_URL')

    product_data = requests.get(f'{product_detail_url}{product_id}/')

    if product_data.status_code == 200:
        product_dict = product_data.json()
        price = product_dict.get('price')

        # Дальнейшая логика (меняем is_active для скрытия продукта с ленты)
        Transaction.objects.filter(id=transaction_id).update(is_accepted=True)
        data = {'is_active': False}
        requests.patch(f'{product_detail_url}{product_id}/', data)

        # Проверка баланса и вычет средств
        acc_from_obj = UserAccount.objects.get(id=acc_from)
        if acc_from_obj.balance >= price:
            UserAccount.objects.filter(id=acc_from).update(balance=F('balance') - price)
            UserAccount.objects.filter(id=acc_to).update(balance=F('balance') + price)
            TransferHistory.objects.create(acc_from=acc_from, acc_to=acc_to, sum=price)
            return {'success': True}
        else:
            return {'error': 'Failed to create transaction, your balance less than price'}
    else:
        return {'error': 'Failed to create transaction'}