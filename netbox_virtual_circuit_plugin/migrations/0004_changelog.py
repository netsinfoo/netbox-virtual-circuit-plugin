# Generated by Django 3.0.8 on 2020-07-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_virtual_circuit_plugin', '0003_vcid_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualcircuit',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='virtualcircuit',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='virtualcircuitvlan',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='virtualcircuitvlan',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
