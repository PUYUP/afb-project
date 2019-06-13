# Generated by Django 2.2 on 2019-05-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_auto_20190521_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='alamat',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='kontak',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='kontakhp',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='kota',
            field=models.CharField(blank=True, db_index=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='namasupplier',
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='teknisi',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='teknisihp',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
