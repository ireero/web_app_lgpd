# Generated by Django 4.0.6 on 2022-08-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
