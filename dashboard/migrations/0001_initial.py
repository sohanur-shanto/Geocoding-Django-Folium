# Generated by Django 3.2.3 on 2021-05-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, null=True)),
                ('population', models.PositiveIntegerField(null=True)),
                ('latitude', models.FloatField(default=0)),
                ('longtitude', models.FloatField(default=0)),
            ],
        ),
    ]