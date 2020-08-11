# Generated by Django 2.2 on 2020-08-10 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_auto_20200811_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userid',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft', models.TextField()),
                ('technical', models.TextField()),
                ('organizational', models.TextField()),
                ('computer', models.TextField()),
                ('language', models.TextField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.user')),
            ],
        ),
    ]