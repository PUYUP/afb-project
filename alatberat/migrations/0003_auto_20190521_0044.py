# Generated by Django 2.2 on 2019-05-20 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alatberat', '0002_auto_20190521_0026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alatberat',
            options={'ordering': ['namaalat'], 'verbose_name': 'Alat Berat', 'verbose_name_plural': 'Alat Berat'},
        ),
        migrations.AlterModelOptions(
            name='hourmeter',
            options={'ordering': ['tanggal'], 'verbose_name': 'Hour Meter', 'verbose_name_plural': 'Hour Meter'},
        ),
        migrations.AlterModelOptions(
            name='operatorab',
            options={'ordering': ['namaoperator'], 'verbose_name': 'Operator Alat Berat', 'verbose_name_plural': 'Operator Alat Berat'},
        ),
        migrations.CreateModel(
            name='Biayaab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(db_index=True)),
                ('biaya', models.DecimalField(decimal_places=2, max_digits=15)),
                ('keterangan', models.TextField(max_length=50)),
                ('alatid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alatberat.Alatberat')),
            ],
            options={
                'verbose_name': 'Biaya',
                'verbose_name_plural': 'Biaya',
                'ordering': ['tanggal'],
            },
        ),
    ]
