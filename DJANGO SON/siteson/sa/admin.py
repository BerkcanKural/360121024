from django.contrib import admin
from .models import kullanici
from .models import kiyafet
from .models import kiyafet_detay
from .models import kiyafet_kategori
from .models import adres
from .models import siparis
from .models import odeme
from .models import sepet


#Register your models here.
admin.site.register(kullanici)
admin.site.register(kiyafet)
admin.site.register(kiyafet_detay)
admin.site.register(kiyafet_kategori)
admin.site.register(adres)
admin.site.register(siparis)
admin.site.register(odeme)
admin.site.register(sepet)
