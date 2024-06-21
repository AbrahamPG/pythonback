# Generated by Django 4.2.7 on 2024-06-03 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('pais', models.CharField(default='', max_length=27)),
                ('dni', models.IntegerField(default='00000000', max_length=8)),
                ('vigente', models.BooleanField(default=True)),
            ],
        ),
    ]
