# Generated by Django 3.2.9 on 2021-12-06 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scraping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(blank=True, db_column='Report', max_length=10, null=True)),
                ('merchant', models.CharField(blank=True, db_column='Merchant', max_length=10, null=True)),
                ('frequency', models.CharField(blank=True, db_column='Frequency', max_length=10, null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=10, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=20, null=True)),
                ('remarks', models.TextField(blank=True, db_column='Remarks', max_length=250, null=True)),
                ('start_time', models.DateTimeField(blank=True, db_column='Start_Time', null=True)),
                ('end_time', models.DateTimeField(blank=True, db_column='End_Time', null=True)),
            ],
        ),
    ]
