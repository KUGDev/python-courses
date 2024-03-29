# Generated by Django 2.2.4 on 2019-08-20 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('riddles', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRiddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt', models.IntegerField()),
                ('riddle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riddles.Riddle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
