# Generated by Django 3.2.13 on 2022-05-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(verbose_name=100)),
                ('name', models.CharField(max_length=500)),
                ('price', models.IntegerField(verbose_name=100)),
                ('company', models.CharField(max_length=500)),
            ],
        ),
    ]
