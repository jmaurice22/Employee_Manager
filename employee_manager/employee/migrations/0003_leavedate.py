# Generated by Django 3.2.8 on 2021-11-06 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='leaveDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(null=True)),
            ],
        ),
    ]