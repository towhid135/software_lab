# Generated by Django 2.2 on 2020-08-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('achievement', models.TextField()),
                ('objective', models.TextField()),
                ('exp', models.TextField()),
            ],
        ),
    ]