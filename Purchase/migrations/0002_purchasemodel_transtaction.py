# Generated by Django 5.1.1 on 2024-12-28 00:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0001_initial'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasemodel',
            name='transtaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='transactions.transactionmodel'),
        ),
    ]
