# Generated by Django 3.0 on 2021-07-02 17:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20210702_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bukuinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('07f8128a-4978-44ae-b6ca-40b8c7ff1396'), primary_key=True, serialize=False),
        ),
    ]