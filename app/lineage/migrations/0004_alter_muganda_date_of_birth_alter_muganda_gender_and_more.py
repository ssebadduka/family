# Generated by Django 4.0.4 on 2022-05-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineage', '0003_alter_muganda_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muganda',
            name='Date_of_birth',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='muganda',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50),
        ),
        migrations.AlterField(
            model_name='muganda',
            name='your_Life_Status',
            field=models.CharField(choices=[('Died', 'Died'), ('Living', 'Living')], default='Living', max_length=100),
        ),
    ]