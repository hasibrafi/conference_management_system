# Generated by Django 2.2.7 on 2021-09-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0014_auto_20210819_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractpaper',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
