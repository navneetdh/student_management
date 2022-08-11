# Generated by Django 4.1 on 2022-08-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='roll_number',
            field=models.IntegerField(),
        ),
    ]