# Generated by Django 4.0.3 on 2022-04-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('features', models.CharField(max_length=20)),
                ('labels', models.CharField(max_length=20)),
            ],
        ),
    ]
