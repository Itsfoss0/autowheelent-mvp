# Generated by Django 4.2.4 on 2023-09-20 19:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_body_style_alter_car_car_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
