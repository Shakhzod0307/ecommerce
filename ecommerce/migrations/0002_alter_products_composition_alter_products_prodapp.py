# Generated by Django 4.1.3 on 2022-12-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='composition',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='prodapp',
            field=models.CharField(max_length=200),
        ),
    ]
