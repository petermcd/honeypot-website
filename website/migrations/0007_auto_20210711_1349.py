# Generated by Django 3.2.5 on 2021-07-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210711_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logins',
            name='host',
            field=models.TextField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='logins',
            name='password',
            field=models.TextField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='logins',
            name='username',
            field=models.TextField(default='', unique=True),
        ),
    ]
