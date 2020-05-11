# Generated by Django 3.0.5 on 2020-05-08 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipam', '0036_standardize_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualCircuit',
            fields=[
                ('vcid', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('status', models.CharField(default='pending-configuration', max_length=30)),
                ('context', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['vcid'],
            },
        ),
        migrations.CreateModel(
            name='VirtualCircuitVLAN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('virtual_circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vlans', to='netbox_virtual_circuit_plugin.VirtualCircuit')),
                ('vlan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vlan_of', to='ipam.VLAN')),
            ],
            options={
                'ordering': ['virtual_circuit'],
            },
        ),
    ]