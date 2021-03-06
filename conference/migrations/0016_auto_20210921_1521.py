# Generated by Django 3.2.5 on 2021-09-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0015_auto_20210913_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractpaper',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='city',
            field=models.CharField(choices=[('Amsterdam', 'Amsterdam'), ('Bengalore', 'Bengalore'), ('California', 'California'), ('Chattogram', 'Chattogram'), ('Dhaka', ''), ('Delhi', 'Delhi'), ('Edmonton', 'Edmonton'), ('Firozabad', 'Firozabad'), ('Greenville', 'Greenville'), ('Ho Chi Minh City', 'Ho Chi Minh City'), ('Ibiza', 'Ibiza'), ('Jessore', 'Jessore'), ('Kualalampur', 'Kualalampur'), ('Melbourne', 'Melbourne'), ('New York', 'New York'), ('Oslo', 'Oslo')], max_length=100),
        ),
        migrations.AlterField(
            model_name='conference',
            name='country',
            field=models.CharField(choices=[('Australia', 'Australia'), ('Algeria', 'Algeria'), ('Bangladesh', 'Bangladesh'), ('Canada', 'Canada'), ('Denmark', 'Denmark'), ('England', 'England'), ('France', 'France'), ('Germany', 'Germany'), ('Hungary', 'Hungary'), ('Italy', 'Italy'), ('Japan', 'Japan'), ('Kenya', 'Kenya'), ('Luxemburg', 'Luxemburg'), ('Mexico', 'Mexico'), ('Norway', 'Norway'), ('Oman', 'Oman')], max_length=100),
        ),
        migrations.AlterField(
            model_name='conference',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='primary_area',
            field=models.CharField(choices=[('Human Computer Interaction', 'Human Computer Interaction'), ('Gamification', 'Gamification'), ('Emerging Technologies', 'Emerging Technologies'), ('Media', 'Media'), ('Communication Networks', 'Communication Networks'), ('Mobile Computing', 'Mobile Computing'), ('Discourse Analysis', 'Discourse Analysis'), ('STEM Education', 'STEM Education'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Microbiology', 'Microbiology'), ('Biochemistry', 'Biochemistry'), ('Mechanic Automation', 'Mechanic Automation'), ('Green Energy', 'Green Energy'), ('Environmental Science', 'Environmental Science'), ('Supply Chain System', 'Supply Chain System'), ('Business Strategy', 'Business Strategy'), ('Literature', 'Literature'), ('Art & Music', 'Art & Music'), ('World Peace & Governance', 'World Peace & Governance')], max_length=255),
        ),
        migrations.AlterField(
            model_name='conference',
            name='secondary_area',
            field=models.CharField(choices=[('Human Computer Interaction', 'Human Computer Interaction'), ('Gamification', 'Gamification'), ('Emerging Technologies', 'Emerging Technologies'), ('Media', 'Media'), ('Communication Networks', 'Communication Networks'), ('Mobile Computing', 'Mobile Computing'), ('Discourse Analysis', 'Discourse Analysis'), ('STEM Education', 'STEM Education'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Microbiology', 'Microbiology'), ('Biochemistry', 'Biochemistry'), ('Mechanic Automation', 'Mechanic Automation'), ('Green Energy', 'Green Energy'), ('Environmental Science', 'Environmental Science'), ('Supply Chain System', 'Supply Chain System'), ('Business Strategy', 'Business Strategy'), ('Literature', 'Literature'), ('Art & Music', 'Art & Music'), ('World Peace & Governance', 'World Peace & Governance')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='type',
            field=models.CharField(choices=[('Conference', 'Conference'), ('Journal', 'Journal'), ('Book', 'Book')], max_length=20),
        ),
    ]
