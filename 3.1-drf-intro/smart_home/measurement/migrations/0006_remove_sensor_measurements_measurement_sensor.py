# Generated by Django 4.1.5 on 2023-02-11 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_alter_measurement_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='measurements',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
    ]
