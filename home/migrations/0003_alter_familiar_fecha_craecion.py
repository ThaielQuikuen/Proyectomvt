# Generated by Django 4.1.1 on 2022-09-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_familiar_fecha_craecion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fecha_craecion',
            field=models.DateField(null=True),
        ),
    ]
