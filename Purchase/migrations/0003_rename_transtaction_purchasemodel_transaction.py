# Generated by Django 5.1.1 on 2024-12-28 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0002_purchasemodel_transtaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasemodel',
            old_name='transtaction',
            new_name='transaction',
        ),
    ]
