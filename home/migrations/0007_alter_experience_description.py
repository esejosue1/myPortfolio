# Generated by Django 4.1.6 on 2023-02-15 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_experience_date_experience_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
