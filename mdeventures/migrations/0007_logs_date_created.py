# Generated by Django 3.1.1 on 2021-12-10 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdeventures', '0006_auto_20211210_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
