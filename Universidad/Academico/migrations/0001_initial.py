# Generated by Django 5.1 on 2024-10-20 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
