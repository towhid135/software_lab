# Generated by Django 2.2 on 2020-08-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_auto_20200811_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]