# Generated by Django 3.2.4 on 2021-06-24 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20210624_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_eat_pizzas', 'Can eat pizzas')]},
        ),
    ]
