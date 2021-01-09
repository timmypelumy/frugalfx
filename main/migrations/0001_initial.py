# Generated by Django 3.1.4 on 2021-01-09 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('wallet_address', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('bonus', models.PositiveIntegerField(default=0)),
                ('notes', models.TextField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PayClaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.PositiveIntegerField()),
                ('curr', models.CharField(max_length=25, verbose_name='Currency')),
                ('sender_addr', models.CharField(max_length=64, verbose_name='Sending Wallet Address')),
                ('description', models.TextField()),
                ('settled', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdraw_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment claim',
                'verbose_name_plural': 'Payment claims',
            },
        ),
    ]
