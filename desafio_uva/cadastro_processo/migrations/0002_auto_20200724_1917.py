# Generated by Django 2.0 on 2020-07-24 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_processo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planilha',
            name='arquivo',
            field=models.FileField(upload_to=''),
        ),
    ]
