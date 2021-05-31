# Generated by Django 3.2.3 on 2021-05-30 23:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.UUIDField(default=uuid.UUID('87922718-1f73-4e58-b27e-0b0d31bc01b6'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='id',
            field=models.UUIDField(default=uuid.UUID('42e28849-7d47-4f2a-899f-1ec24269f894'), editable=False, primary_key=True, serialize=False),
        ),
    ]