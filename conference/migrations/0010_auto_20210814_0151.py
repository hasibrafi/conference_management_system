# Generated by Django 2.2.7 on 2021-08-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0009_auto_20210814_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractpaper',
            name='abstract_file',
            field=models.FileField(upload_to='media/uploads/'),
        ),
    ]
