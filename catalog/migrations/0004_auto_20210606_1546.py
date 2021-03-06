# Generated by Django 3.0 on 2021-06-06 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_auto_20210606_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bukuinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2c4d2ede-f049-4402-9d67-88da44d88323'), primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelas', models.CharField(blank=True, max_length=120)),
                ('nis', models.CharField(blank=True, max_length=120)),
                ('telepon', models.CharField(max_length=20)),
                ('url_foto', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
