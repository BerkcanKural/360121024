# Generated by Django 4.0 on 2022-11-14 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('kullanici_id', models.CharField(max_length=10)),
                ('kullanici_sehir', models.CharField(max_length=25)),
                ('kullanici_adres', models.CharField(max_length=250)),
                ('kullanici_adres_satir2', models.CharField(max_length=250)),
                ('kullanici_posta_kod', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='kiyafet',
            fields=[
                ('kiyafet_id', models.AutoField(primary_key=True, serialize=False)),
                ('kiyafet_cinsiyet', models.CharField(max_length=15)),
                ('kiyafet_foto', models.ImageField(upload_to='static/')),
                ('kiyafet_fiyat', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='kiyafet_detay',
            fields=[
                ('kiyafet_id', models.AutoField(primary_key=True, serialize=False)),
                ('kiyafet_title', models.CharField(max_length=150)),
                ('kiyafet_desc', models.CharField(max_length=200)),
                ('kiyafet_beden', models.CharField(max_length=4)),
                ('kiyafet_kumas', models.CharField(max_length=20)),
                ('kiyafet_renk', models.CharField(max_length=15)),
                ('kiyafet_desen', models.BooleanField(default=False)),
                ('kiyafet_stok', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='kiyafet_kategori',
            fields=[
                ('kiyafet_id', models.AutoField(primary_key=True, serialize=False)),
                ('kiyafet_tipi', models.CharField(max_length=25)),
                ('kiyafet_sezon', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='kullanici',
            fields=[
                ('kullanici_id', models.AutoField(primary_key=True, serialize=False)),
                ('kullanici_ad', models.CharField(max_length=25)),
                ('kullanici_sifre', models.CharField(max_length=15)),
                ('kullanici_telno', models.CharField(max_length=14)),
                ('kullanici_hesapOlusturma_tarih', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='siparis',
            fields=[
                ('siparis_id', models.AutoField(primary_key=True, serialize=False)),
                ('siparis_no', models.CharField(max_length=15)),
                ('siparis_tarih', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('kullanici_id', models.CharField(max_length=10)),
                ('kullanici_adres', models.CharField(max_length=250)),
                ('kullanici_adres_satir2', models.CharField(max_length=250)),
                ('teslim_edildi', models.BooleanField(default=False)),
            ],
        ),
    ]
