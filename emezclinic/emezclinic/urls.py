from django.contrib import admin
from django.urls import path
from emez.views import *  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing"),
    path('pembayaran/', pembayaran, name='pembayaran'),
    path('bukti_pembayaran/', bukti_pembayaran, name='bukti_pembayaran'),
    path('form_penilaian/', form_penilaian, name='form_penilaian'),
    path('history_pemesanan/', history_pemesanan, name='history_pemesanan'),
    path('pilih_dokter/', pilih_dokter, name='pilih_dokter'),
    path('formulir/', formulir, name='formulir'),
    path('profile/', profile, name='profile'),
    path('pilih_jadwal/', pilih_jadwal, name='pilih_jadwal'),

]
