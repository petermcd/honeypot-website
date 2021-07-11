# Generated by Django 3.2.5 on 2021-07-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_setting_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logins',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=15, unique=True)),
                ('username', models.CharField(max_length=2000, unique=True)),
                ('password', models.CharField(max_length=2000, unique=True)),
                ('processed', models.IntegerField(default=0)),
                ('when', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]