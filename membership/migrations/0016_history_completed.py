# Generated by Django 3.1 on 2020-08-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0015_auto_20200828_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='후기유무'),
        ),
    ]
