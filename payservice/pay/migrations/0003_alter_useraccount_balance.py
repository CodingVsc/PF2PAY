# Generated by Django 4.2.3 on 2023-07-20 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0002_alter_useraccount_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
