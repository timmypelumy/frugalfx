# Generated by Django 3.1.3 on 2020-12-10 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='currency_type',
            field=models.CharField(choices=[('Bitcoin', 'Bitcoin'), ('Fortron', 'Fortron'), ('Ethereum', 'Ethereum'), ('Litecoin', 'Litecoin')], default='Bitcoin', max_length=15),
        ),
    ]