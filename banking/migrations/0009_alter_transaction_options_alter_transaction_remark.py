# Generated by Django 5.0.4 on 2024-08-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banking", "0008_alter_transaction_amount_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transaction",
            options={"ordering": ["-created"]},
        ),
        migrations.AlterField(
            model_name="transaction",
            name="remark",
            field=models.CharField(blank=True, null=True),
        ),
    ]
