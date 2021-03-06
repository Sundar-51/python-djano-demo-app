# Generated by Django 2.2.14 on 2022-01-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplecheckboxapp', '0002_auto_20220120_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsearch',
            name='job',
            field=models.CharField(choices=[('Engineer', 'Engineer'), ('Testing', 'Testing'), ('Manager', 'Manager')], default='Engineer', max_length=25),
        ),
        migrations.AlterField(
            model_name='jobsearch',
            name='location',
            field=models.CharField(choices=[('Chennai', 'Chennai'), ('Bangalore', 'Bangalore'), ('Hyderabad', 'Hyderabad')], default='Chennai', max_length=25),
        ),
        migrations.AlterField(
            model_name='jobsearch',
            name='salary',
            field=models.CharField(choices=[('0-20K', '0-20K'), ('20-40K', '20-40K'), ('40-60K', '40-60K')], default='0-20K', max_length=25),
        ),
    ]
