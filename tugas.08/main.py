# ============================================
# SOAL 1 - Layout Papan Catur
# ============================================


HITAM = "⬛"    # emoji kotak hitam
PUTIH = "⬜"    # emoji kotak putih
UKURAN = 8       # ukuran papan (bisa diubah)

print("=" * 18)
print("  PAPAN CATUR 8x8")
print("=" * 18)

for baris in range(UKURAN):
    for kolom in range(UKURAN):
        if (baris + kolom) % 2 == 0:
            print(PUTIH, end="")
        else:
            print(HITAM, end="")
    print()  # newline setelah tiap baris selesai

print("=" * 18)
print(f"Total kotak : {UKURAN * UKURAN}")
print(f"Kotak hitam : {UKURAN * UKURAN // 2}")
print(f"Kotak putih : {UKURAN * UKURAN // 2}")

# ================================================
# SOAL 2 - Program Manajemen Aktivitas Harian
# Aktivitas: Memasak, Berkebun, Bernyanyi, Olahraga
# Improvisasi: Pengingat lucu dengan kaomoji
# ================================================

from datetime import datetime
import random

# -----------------------------------------------
# (b) List kosong untuk menyimpan aktivitas user
# -----------------------------------------------
aktivitas_list = []

# -----------------------------------------------
# Daftar pilihan aktivitas
# -----------------------------------------------
PILIHAN_AKTIVITAS = {
    "1": "Memasak",
    "2": "Berkebun",
    "3": "Bernyanyi",
    "4": "Olahraga"
}

# -----------------------------------------------
# Improvisasi: Kumpulan pengingat lucu per aktivitas
# Ditampilkan secara acak setelah user input aktivitas
# -----------------------------------------------
PENGINGAT = {
    "Memasak": [
        "(>_<)  Jangan lupa cuci tangan dulu ya sebelum masak!",
        "( >w<) Cicipin dulu sebelum disajiin, biar gak keasinan!",
        "(^.^)/ Masak pakai hati, hasilnya pasti enak~",
        "(OwO)  Api jangan terlalu besar ya, nanti gosong loh!",
        "(T_T)/ Jangan lupa matiin kompor setelah selesai!",
    ],
    "Berkebun": [
        "(^▽^)  Siram tanamannya pagi atau sore ya, bukan siang!",
        "(*^_^*)Tanaman juga butuh cinta, ajak ngobrol dikit~",
        "(o.O)  Pakai sarung tangan biar tangannya gak kotor!",
        "(>.<)  Jangan lupa cabut rumputnya yang liar ya!",
        "(.w.)  Siramlah secukupnya, kebanyakan air juga gak bagus~",
    ],
    "Bernyanyi": [
        "(^o^)/  Pemanasan dulu yuk, biar suaranya gak serak!",
        "(*≧ω≦) Nyanyi dari hati, fals pun jadi merdu~",
        "(>w<)  Minum air putih yang banyak biar tenggorokan oke!",
        "( ^▽^) Jangan malu nyanyi keras-keras, rumahmu, aturanmu!",
        "(o^▽^o)Rekam suaramu, siapa tau jadi viral besok!",
    ],
    "Olahraga": [
        "(>_<)/  Pemanasan dulu 5 menit biar gak kram ya!",
        "(*^▽^*) Minum air putih yang cukup selama olahraga!",
        "(T▽T)  Jangan langsung tiduran setelah olahraga!",
        "(^v^)/  Konsisten itu kunci, semangat terus ya!",
        "(o_O)   Pakai sepatu yang nyaman biar kaki gak sakit~",
    ],
}

# -----------------------------------------------
# Fungsi: tampilkan pengingat acak
# -----------------------------------------------
def tampilkan_pengingat(nama_aktivitas):
    print("\n  +------------------------------------------+")
    print("  |  (!) PENGINGAT UNTUKMU                  |")
    pesan = random.choice(PENGINGAT[nama_aktivitas])
    print(f"  |  {pesan:<40}|")
    print("  +------------------------------------------+")

# -----------------------------------------------
# Fungsi: tampilkan header
# -----------------------------------------------
def tampilkan_header():
    print("\n" + "=" * 50)
    print("  (^_^)/ MANAJEMEN AKTIVITAS HARIAN")
    print("=" * 50)
    print("  Hai! Yuk catat aktivitasmu hari ini~ (>w<)")

# -----------------------------------------------
# (a) Fungsi: input aktivitas dari user
# -----------------------------------------------
def tambah_aktivitas():
    print("\n  Pilih aktivitas yang mau dicatat:")
    for kode, nama in PILIHAN_AKTIVITAS.items():
        print(f"    {kode}. {nama}")

    pilih = input("\n  Ketik nomornya [1-4]: ").strip()

    if pilih not in PILIHAN_AKTIVITAS:
        print("  (>_<) Nomornya salah! Coba lagi ya.")
        return

    nama_aktivitas = PILIHAN_AKTIVITAS[pilih]

    # Tampilkan pengingat lucu setelah pilih aktivitas
    tampilkan_pengingat(nama_aktivitas)

    # -----------------------------------------------
    # (d) Input tambahan berkaitan dengan aktivitas
    # -----------------------------------------------
    print(f"\n  --- Detail Aktivitas: {nama_aktivitas} ---")
    waktu    = input("  Waktu (pagi/siang/sore/malam) : ").strip()
    durasi   = input("  Durasi (menit)                : ").strip()
    lokasi   = input("  Lokasi kegiatan               : ").strip()
    perasaan = input("  Perasaan setelahnya           : ").strip()
    catatan  = input("  Catatan tambahan              : ").strip()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # (b) Masukkan ke dalam list kosong
    aktivitas_list.append({
        "aktivitas" : nama_aktivitas,
        "waktu"     : waktu     if waktu     else "tidak diisi",
        "durasi"    : durasi    if durasi    else "0",
        "lokasi"    : lokasi    if lokasi    else "tidak diisi",
        "perasaan"  : perasaan  if perasaan  else "tidak diisi",
        "catatan"   : catatan   if catatan   else "-",
        "timestamp" : timestamp,
    })

    print(f"\n  (^▽^)/ Yeay! '{nama_aktivitas}' berhasil dicatat!")
    print(f"         Total tersimpan: {len(aktivitas_list)} aktivitas")

# -----------------------------------------------
# (c) Fungsi: cetak semua aktivitas dari list
# -----------------------------------------------
def cetak_semua_aktivitas():
    if not aktivitas_list:
        print("\n  (T_T) Belum ada aktivitas nih... Yuk tambah dulu!")
        return

    print("\n" + "=" * 50)
    print(f"  (*^_^*) DAFTAR AKTIVITASMU [{len(aktivitas_list)} data]")
    print("=" * 50)

    for i, data in enumerate(aktivitas_list, start=1):
        print(f"\n  [{i}] Aktivitas  : {data['aktivitas']}")
        print(f"       Waktu      : {data['waktu']}")
        print(f"       Durasi     : {data['durasi']} menit")
        print(f"       Lokasi     : {data['lokasi']}")
        print(f"       Perasaan   : {data['perasaan']}")
        print(f"       Catatan    : {data['catatan']}")
        print(f"       Dicatat    : {data['timestamp']}")
        print("       " + "-" * 38)

    total = sum(int(d["durasi"]) for d in aktivitas_list if d["durasi"].isdigit())
    print(f"\n  Total durasi : {total} menit")

    # Pengingat penutup acak
    penutup = [
        "(>w<)  Kamu produktif banget hari ini, keren!",
        "(^o^)/ Pertahankan semangat ini ya~",
        "(*^▽^*)Aktivitasmu kece abis, keep it up!",
        "(^_-)-  Istirahat yang cukup juga penting loh!",
    ]
    print(f"\n  {random.choice(penutup)}")
    print("=" * 50)

# -----------------------------------------------
# PROGRAM UTAMA
# -----------------------------------------------
tampilkan_header()

while True:
    print("\n  MENU:")
    print("  1. Tambah aktivitas")
    print("  2. Lihat semua aktivitas")
    print("  3. Keluar")

    menu = input("\n  Pilih menu [1/2/3]: ").strip()

    if menu == "1":
        tambah_aktivitas()
    elif menu == "2":
        cetak_semua_aktivitas()     # (c) cetak semua aktivitas
    elif menu == "3":
        cetak_semua_aktivitas()
        print("\n  (^_^)/ Sampai jumpa! Jangan lupa istirahat ya~\n")
        break
    else:
        print("  (o_O) Menu-nya salah nih, coba 1, 2, atau 3!")
