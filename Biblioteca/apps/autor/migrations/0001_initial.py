# Generated by Django 3.1.5 on 2021-01-08 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=30)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('edad', models.PositiveIntegerField()),
            ],
        ),
    ]
