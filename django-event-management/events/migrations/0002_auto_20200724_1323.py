# Generated by Django 2.2.13 on 2020-07-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoin',
            name='gain_type',
            field=models.CharField(choices=[('event', 'Event'), ('others', 'Others')], max_length=6),
        ),
    ]
