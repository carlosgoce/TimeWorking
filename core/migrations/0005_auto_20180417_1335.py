# Generated by Django 2.0.4 on 2018-04-17 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180417_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityjournal',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registry',
            name='end',
            field=models.DateTimeField(blank=True),
        ),
    ]