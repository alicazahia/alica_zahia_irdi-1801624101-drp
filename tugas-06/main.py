# IF STATEMENT

# Aktivitas Sarapan

# INPUT
sarapan = True  # kegiatan yang dilakukan
menu = "roti"  # menu yang dipilih

if menu == "roti":
    perlu_masak = True
elif menu == "sayur":
    perlu_masak = True
elif menu == "daging":
    perlu_masak = True
else:
    perlu_masak = False

# OUT
if perlu_masak:
    print("Bahan tersedia, silakan masak terlebih dahulu!")
else:
    print("Bahan tidak tersedia, beli terlebih dahulu!")

# Aktivitas Berangkat Kerja

# INPUT
from datetime import datetime
waktu_sekarang = datetime.now()
jam_masuk = waktu_sekarang.replace(hour=8, minute=0, second=0, microsecond=0)
terlambat = waktu_sekarang > jam_masuk

# OUT
if terlambat:
    print("Kamu terlambat masuk kerja!")
else:
    print("Kamu belum terlambat, semangat!")
    