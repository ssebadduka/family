# Generated by Django 4.0.4 on 2022-05-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='muganda',
            name='Age',
        ),
        migrations.AddField(
            model_name='muganda',
            name='Date_of_birth',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
