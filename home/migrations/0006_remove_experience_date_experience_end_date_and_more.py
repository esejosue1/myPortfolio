# Generated by Django 4.1.6 on 2023-02-15 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='date',
        ),
        migrations.AddField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]