# Generated by Django 4.1.5 on 2023-01-13 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_knowledge'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledge',
            name='bar_level',
            field=models.CharField(default=0, max_length=3),
        ),
    ]
