# Generated by Django 4.0.5 on 2022-06-21 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=200)),
                ('customer_ip', models.CharField(max_length=30, null=True)),
                ('issued_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
