# Generated by Django 2.2.4 on 2019-08-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0003_userriddle'),
    ]

    operations = [
        migrations.AddField(
            model_name='userriddle',
            name='time_spent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
