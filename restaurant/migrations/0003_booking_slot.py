# Generated by Django 5.0.1 on 2024-03-04 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_menuitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='slot',
            field=models.SmallIntegerField(default=10),
        ),
    ]