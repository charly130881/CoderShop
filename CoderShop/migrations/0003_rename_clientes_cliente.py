# Generated by Django 4.0.1 on 2022-01-24 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoderShop', '0002_rename_vendedores_vendedor_alter_clientes_telefono'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
    ]