from django.db import models
import datetime
# Create your models here.

class kiyafet(models.Model):
    kiyafet_id = models.AutoField(primary_key=True)
    kiyafet_cinsiyet = models.CharField(max_length=15)    #kadın-erkek-unisex    
    kiyafet_foto = models.ImageField(upload_to='static/') #kiyafet fotosu    
    kiyafet_fiyat = models.FloatField(max_length=8)        #kiyafet fiyat
    
class kiyafet_detay(models.Model):
    kiyafet_id = models.AutoField(primary_key=True)
    kiyafet_title = models.CharField(max_length=150)
    kiyafet_desc = models.CharField(max_length=200)      #kıyafet açıklaması
    kiyafet_beden = models.CharField(max_length=4)       #kiyafet beden          
    kiyafet_kumas = models.CharField(max_length=20)      # kumas tipi
    kiyafet_renk = models.CharField(max_length=15)       # kiyafet rengi
    kiyafet_desen = models.BooleanField(default=False)   # desen-baskı var mı yok mu
    kiyafet_stok = models.CharField(max_length=4)        # stok sayisi

class kiyafet_kategori(models.Model):
    kiyafet_id = models.AutoField(primary_key=True)
    kiyafet_tipi = models.CharField(max_length=25)       # şort tişort sweat vs
    kiyafet_sezon = models.CharField(max_length=10)      # yaz kış 

class kullanici(models.Model):
    kullanici_id = models.AutoField(primary_key=True)
    kullanici_ad = models.CharField(max_length=25)
    kullanici_sifre = models.CharField(max_length=15)
    kullanici_telno = models.CharField(max_length=14)
    kullanici_hesapOlusturma_tarih = models.DateField(("Date"), default=datetime.date.today)

class adres(models.Model):
    adress_id = models.AutoField(primary_key=True)
    kullanici_id = models.IntegerField()
    kullanici_sehir = models.CharField(max_length=25)
    kullanici_adres = models.CharField(max_length=250)
    kullanici_adres_satir2 = models.CharField(max_length=250)  #gerekirse
    kullanici_posta_kod = models.CharField(max_length=5)


class siparis(models.Model):
    siparis_id = models.AutoField(primary_key=True)
    siparis_no = models.CharField(max_length=15)
    siparis_tarih = models.DateField(("Date"), default=datetime.date.today)
    kullanici_id = models.IntegerField()
    kullanici_adres = models.CharField(max_length=250)
    kullanici_adres_satir2 = models.CharField(max_length=250)  #gerekirse
    teslim_edildi = models.BooleanField(default=False)

class odeme(models.Model):
    kart_id = models.AutoField(primary_key=True)
    kullanici_id = models.IntegerField()
    kart_no = models.CharField(max_length=16)
    kart_skt = models.CharField(max_length=4)
    kart_cvv = models.CharField(max_length=3)

class sepet(models.Model):
    sepet_id= models.AutoField(primary_key=True)
    kiyafet_id = models.IntegerField()
    kiyafet_title = models.CharField(max_length=150)
    kiyafet_desc = models.CharField(max_length=200) 
    sepet_toplam_fiyat = models.CharField(max_length=5)


