from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html')
def pembayaran(request):
    return render(request, 'pembayaran.html')
def bukti_pembayaran(request):
    return render(request, 'bukti_pembayaran.html')
def form_penilaian(request):
    return render(request, 'form_penilaian.html')
def history_pemesanan(request):
    return render(request, 'history_pemesanan.html')
def pilih_dokter(request):
    return render(request, 'pilih_dokter.html')
def formulir(request):
    return render(request, 'formulir.html')
def profile(request):
    return render(request, 'profile.html')
def pilih_jadwal(request):
    # Your view logic here
    return render(request, 'pilih_jadwal.html')