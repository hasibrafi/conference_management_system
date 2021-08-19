# Generated by Django 3.2.5 on 2021-08-11 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0007_auto_20210811_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abstractpaper',
            name='conference',
        ),
        migrations.AddField(
            model_name='abstractpaper',
            name='conference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='conference.conference'),
        ),
    ]