# Generated by Django 4.0.4 on 2022-05-11 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineage', '0004_alter_muganda_date_of_birth_alter_muganda_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muganda',
            name='Date_of_birth',
            field=models.DateField(),
        ),
    ]
