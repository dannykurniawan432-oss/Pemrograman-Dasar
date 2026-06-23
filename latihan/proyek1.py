"""
===========================================================
💰 PROGRAM: SISTEM MANAJEMEN KEUANGAN PRIBADI
===========================================================
Tujuan:
Program ini dibuat untuk membantu pengguna mengatur keuangan pribadi.
Dengan program ini pengguna dapat:
- Mencatat pemasukan dan pengeluaran uang
- Melihat seluruh transaksi yang pernah dicatat
- Mengetahui saldo akhir saat ini
- Melihat analisis pengeluaran berdasarkan kategori
- Menyimpan data ke file agar tidak hilang

Konsep Python yang digunakan:
✅ Variabel, List, Dictionary
✅ Fungsi (def)
✅ Percabangan (if-elif-else)
✅ Perulangan (for, while)
✅ Exception handling (try-except)
✅ File handling (open, read, write)
===========================================================
"""

import datetime  # Library datetime digunakan untuk mengambil tanggal otomatis


# =========================================================
# Bagian 1: Inisialisasi Data
# =========================================================
# Di sini kita membuat list kosong untuk menyimpan data transaksi.
# Setiap transaksi nanti akan disimpan dalam bentuk dictionary.
data_keuangan = []


# =========================================================
# Bagian 2: Fungsi Tambah Transaksi
# =========================================================
def tambah_transaksi():
    """
    Fungsi ini dipanggil ketika pengguna ingin menambah transaksi baru.
    Transaksi bisa berupa pemasukan (uang masuk) atau pengeluaran (uang keluar).
    """
    try:
        # Meminta input dari pengguna tentang jenis transaksi
        jenis = input("Jenis (pemasukan/pengeluaran): ").lower()

        # Mengecek apakah input jenis valid
        if jenis not in ["pemasukan", "pengeluaran"]:
            print("⚠ Jenis tidak valid! Harus 'pemasukan' atau 'pengeluaran'.\n")
            return  # Menghentikan fungsi jika input salah

        # Meminta deskripsi transaksi, misalnya “Gaji”, “Makan siang”, dsb
        deskripsi = input("Deskripsi: ")

        # Meminta jumlah uang (harus berupa angka)
        jumlah = int(input("Jumlah uang (Rp): "))

        # Jika transaksi berupa pengeluaran, minta kategori tambahan
        kategori = "-"
        if jenis == "pengeluaran":
            kategori = input("Kategori (makanan, transport, hiburan, dll): ").lower()

        # Membuat data transaksi dalam bentuk dictionary
        transaksi = {
            "tanggal": datetime.date.today().strftime("%d-%m-%Y"),  # tanggal otomatis hari ini
            "jenis": jenis,
            "deskripsi": deskripsi,
            "kategori": kategori,
            "jumlah": jumlah
        }

        # Menambahkan transaksi ke dalam list utama (data_keuangan)
        data_keuangan.append(transaksi)
        print("✅ Transaksi berhasil ditambahkan!\n")

    except ValueError:
        # Jika pengguna memasukkan jumlah uang bukan angka
        print("⚠ Jumlah harus berupa angka!\n")


# =========================================================
# Bagian 3: Fungsi Menampilkan Transaksi
# =========================================================
def tampilkan_transaksi():
    """
    Fungsi ini menampilkan semua transaksi yang sudah dimasukkan.
    Data ditampilkan dalam bentuk tabel agar mudah dibaca.
    """
    # Mengecek apakah data transaksi kosong
    if not data_keuangan:
        print("Belum ada transaksi!\n")
        return

    # Menampilkan header tabel
    print("\n=== Daftar Transaksi ===")
    print(f"{'Tanggal':<12} {'Jenis':<15} {'Deskripsi':<15} {'Kategori':<15} {'Jumlah (Rp)':>10}")
    print("-"*70)

    # Menggunakan perulangan untuk menampilkan setiap transaksi
    for d in data_keuangan:
        print(f"{d['tanggal']:<12} {d['jenis']:<15} {d['deskripsi']:<15} {d['kategori']:<15} {d['jumlah']:>10}")

    print("-"*70, "\n")


# =========================================================
# Bagian 4: Fungsi Hitung Saldo
# =========================================================
def hitung_saldo():
    """
    Fungsi ini menghitung saldo akhir pengguna.
    Caranya adalah dengan menambahkan semua pemasukan dan mengurangkan pengeluaran.
    """
    saldo = 0  # Variabel untuk menyimpan saldo total

    # Menggunakan perulangan untuk membaca semua transaksi
    for d in data_keuangan:
        if d['jenis'] == 'pemasukan':
            saldo += d['jumlah']  # Tambahkan ke saldo
        else:
            saldo -= d['jumlah']  # Kurangkan dari saldo

    # Menampilkan hasil saldo
    print(f"💵 Saldo saat ini: Rp {saldo:,}\n")


# =========================================================
# Bagian 5: Fungsi Analisis Pengeluaran
# =========================================================
def analisis_pengeluaran():
    """
    Fungsi ini menganalisis total pengeluaran berdasarkan kategori.
    Tujuannya agar pengguna tahu kategori mana yang paling banyak menghabiskan uang.
    """
    pengeluaran = {}  # Dictionary untuk menyimpan total per kategori
    total = 0  # Total seluruh pengeluaran

    # Perulangan untuk membaca semua data
    for d in data_keuangan:
        if d["jenis"] == "pengeluaran":
            total += d["jumlah"]  # Tambah ke total semua pengeluaran
            # Jika kategori sudah ada, tambahkan jumlahnya; jika belum, buat baru
            pengeluaran[d["kategori"]] = pengeluaran.get(d["kategori"], 0) + d["jumlah"]

    # Jika belum ada pengeluaran, tampilkan pesan
    if not pengeluaran:
        print("Belum ada data pengeluaran!\n")
        return

    print("\n=== Analisis Pengeluaran per Kategori ===")
    # Menampilkan tiap kategori dan jumlahnya
    for kategori, jumlah in pengeluaran.items():
        persen = (jumlah / total) * 100  # Menghitung persentase tiap kategori
        print(f"{kategori.capitalize():<15} : Rp {jumlah:>10,} ({persen:.1f}%)")

    # Menampilkan total pengeluaran
    print(f"Total Pengeluaran: Rp {total:,}\n")


# =========================================================
# Bagian 6: Fungsi Simpan Data ke File
# =========================================================
def simpan_data():
    """
    Fungsi ini menyimpan semua data transaksi ke file teks (keuangan.txt).
    Tujuannya agar data tetap ada walaupun program ditutup.
    """
    with open("keuangan.txt", "w") as file:
        # Menulis setiap transaksi ke file dalam format CSV (dipisah koma)
        for d in data_keuangan:
            file.write(f"{d['tanggal']},{d['jenis']},{d['deskripsi']},{d['kategori']},{d['jumlah']}\n")
    print("💾 Data berhasil disimpan ke file keuangan.txt!\n")


# =========================================================
# Bagian 7: Fungsi Muat Data dari File
# =========================================================
def muat_data():
    """
    Fungsi ini membaca data dari file keuangan.txt (jika ada),
    dan menambahkannya ke list data_keuangan agar bisa dilanjutkan.
    """
    try:
        with open("keuangan.txt", "r") as file:
            for line in file:
                # Memecah tiap baris berdasarkan koma
                tgl, jenis, desk, kat, jml = line.strip().split(",")
                # Menambahkan hasilnya ke list data_keuangan
                data_keuangan.append({
                    "tanggal": tgl,
                    "jenis": jenis,
                    "deskripsi": desk,
                    "kategori": kat,
                    "jumlah": int(jml)
                })
        print("📂 Data berhasil dimuat dari file!\n")
    except FileNotFoundError:
        # Jika file belum ada, tampilkan pesan dan lanjut tanpa error
        print("⚠ File belum ditemukan, mulai dengan data baru.\n")


# =========================================================
# Bagian 8: Menu Utama Program
# =========================================================
def menu():
    """
    Fungsi untuk menampilkan pilihan menu ke pengguna.
    Menu ini akan muncul setiap kali pengguna selesai melakukan aksi.
    """
    print("="*50)
    print("💰 SISTEM MANAJEMEN KEUANGAN PRIBADI 💰")
    print("="*50)
    print("1. Tambah Transaksi")
    print("2. Lihat Semua Transaksi")
    print("3. Lihat Saldo Saat Ini")
    print("4. Analisis Pengeluaran 📊")
    print("5. Simpan Data ke File")
    print("6. Muat Data dari File")
    print("7. Keluar Program")
    print("="*50)


# =========================================================
# Bagian 9: Program Utama (Main Loop)
# =========================================================
# Program utama menggunakan perulangan while agar terus berjalan
# sampai pengguna memilih untuk keluar (pilihan 7).

muat_data()  # Saat program dibuka, coba muat data dari file dulu

while True:
    menu()  # Tampilkan menu
    try:
        # Meminta input pilihan pengguna
        pilih = int(input("Pilih menu (1-7): "))

        # Mengecek pilihan dan menjalankan fungsi sesuai menu
        if pilih == 1:
            tambah_transaksi()
        elif pilih == 2:
            tampilkan_transaksi()
        elif pilih == 3:
            hitung_saldo()
        elif pilih == 4:
            analisis_pengeluaran()
        elif pilih == 5:
            simpan_data()
        elif pilih == 6:
            muat_data()
        elif pilih == 7:
            # Jika pengguna memilih keluar, hentikan loop
            print("👋 Terima kasih telah menggunakan program ini!")
            break
        else:
            print("⚠ Pilihan tidak ada!\n")

    except ValueError:
        # Menangani error jika input bukan angka
        print("⚠ Masukkan angka saja!\n")

