# Generated by Django 2.0.8 on 2018-12-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_paymentsos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsosnotification',
            name='sub_category',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
