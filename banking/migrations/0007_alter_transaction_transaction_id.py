# Generated by Django 5.0.4 on 2024-08-22 10:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banking", "0006_alter_account_account_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
