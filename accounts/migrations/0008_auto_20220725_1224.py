# Generated by Django 3.2.7 on 2022-07-25 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220725_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbase',
            name='in_staking',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='in_wallet_amount',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='withdrawn_amount',
        ),
    ]