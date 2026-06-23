"""
===========================================================
📇 PROGRAM: SISTEM MANAJEMEN KONTAK (VERSI LANJUTAN)
===========================================================
Tujuan:
Program ini membantu pengguna mengelola kontak lebih lengkap:
- Menambah, melihat, mencari, menghapus kontak
- Mengedit kontak
- Mengurutkan daftar kontak berdasarkan nama
- Menyimpan & memuat data ke/dari file

Konsep Python yang digunakan:
✅ Variabel, List, Dictionary
✅ Fungsi (def)
✅ Percabangan (if-elif-else)
✅ Perulangan (for, while)
✅ Exception handling (try-except)
✅ File handling (open, read, write)
✅ Sorting list of dictionaries
===========================================================
"""
import json

# =========================================================
# Bagian 1: Inisialisasi Data
# =========================================================
data_kontak = []

# =========================================================
# Bagian 2: Fungsi Tambah Kontak
# =========================================================
def tambah_kontak():
    nama = input("Nama: ").strip()
    no_telp = input("Nomor Telepon: ").strip()
    email = input("Email: ").strip()

    kontak = {"nama": nama, "no_telp": no_telp, "email": email}
    data_kontak.append(kontak)
    print("✅ Kontak berhasil ditambahkan!\n")

# =========================================================
# Bagian 3: Fungsi Tampilkan Semua Kontak
# =========================================================
def tampilkan_kontak(urut=False):
    if not data_kontak:
        print("Belum ada kontak!\n")
        return

    daftar = sorted(data_kontak, key=lambda k: k['nama'].lower()) if urut else data_kontak

    print("\n=== Daftar Kontak ===")
    print(f"{'Nama':<20} {'Nomor Telepon':<15} {'Email':<25}")
    print("-"*60)
    for k in daftar:
        print(f"{k['nama']:<20} {k['no_telp']:<15} {k['email']:<25}")
    print("-"*60, "\n")

# =========================================================
# Bagian 4: Fungsi Cari Kontak
# =========================================================
def cari_kontak():
    keyword = input("Masukkan nama yang dicari: ").lower()
    hasil = [k for k in data_kontak if keyword in k['nama'].lower()]

    if not hasil:
        print("⚠ Kontak tidak ditemukan!\n")
        return

    print("\n=== Hasil Pencarian ===")
    print(f"{'Nama':<20} {'Nomor Telepon':<15} {'Email':<25}")
    print("-"*60)
    for k in hasil:
        print(f"{k['nama']:<20} {k['no_telp']:<15} {k['email']:<25}")
    print("-"*60, "\n")

# =========================================================
# Bagian 5: Fungsi Hapus Kontak
# =========================================================
def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ").lower()
    global data_kontak
    awal = len(data_kontak)
    data_kontak = [k for k in data_kontak if k['nama'].lower() != nama]

    if len(data_kontak) < awal:
        print("✅ Kontak berhasil dihapus!\n")
    else:
        print("⚠ Kontak tidak ditemukan!\n")

# =========================================================
# Bagian 6: Fungsi Edit Kontak
# =========================================================
def edit_kontak():
    nama = input("Masukkan nama kontak yang ingin diedit: ").lower()
    found = False
    for k in data_kontak:
        if k['nama'].lower() == nama:
            found = True
            print("Kontak ditemukan. Biarkan kosong jika tidak ingin mengubah.")
            nama_baru = input(f"Nama baru ({k['nama']}): ").strip()
            no_telp_baru = input(f"Nomor Telepon baru ({k['no_telp']}): ").strip()
            email_baru = input(f"Email baru ({k['email']}): ").strip()

            if nama_baru: k['nama'] = nama_baru
            if no_telp_baru: k['no_telp'] = no_telp_baru
            if email_baru: k['email'] = email_baru
            print("✅ Kontak berhasil diperbarui!\n")
            break
    if not found:
        print("⚠ Kontak tidak ditemukan!\n")

# =========================================================
# Bagian 7: Fungsi Simpan Data ke File
# =========================================================
def simpan_data():
    with open("kontak.json", "w") as file:
        json.dump(data_kontak, file, indent=4)
    print("💾 Data berhasil disimpan ke file kontak.json!\n")

# =========================================================
# Bagian 8: Fungsi Muat Data dari File
# =========================================================
def muat_data():
    global data_kontak
    try:
        with open("kontak.json", "r") as file:
            data_kontak = json.load(file)
        print("📂 Data berhasil dimuat dari file!\n")
    except FileNotFoundError:
        print("⚠ File belum ditemukan, mulai dengan data baru.\n")

# =========================================================
# Bagian 9: Menu Utama Program
# =========================================================
def menu():
    print("="*50)
    print("📇 SISTEM MANAJEMEN KONTAK LANJUTAN 📇")
    print("="*50)
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak 🔍")
    print("4. Hapus Kontak ❌")
    print("5. Edit Kontak ✏️")
    print("6. Urutkan Kontak berdasarkan Nama ⬆️")
    print("7. Simpan Data ke File")
    print("8. Muat Data dari File")
    print("9. Keluar Program")
    print("="*50)

# =========================================================
# Bagian 10: Program Utama (Main Loop)
# =========================================================
muat_data()

while True:
    menu()
    try:
        pilih = int(input("Pilih menu (1-9): "))
        if pilih == 1:
            tambah_kontak()
        elif pilih == 2:
            tampilkan_kontak()
        elif pilih == 3:
            cari_kontak()
        elif pilih == 4:
            hapus_kontak()
        elif pilih == 5:
            edit_kontak()
        elif pilih == 6:
            tampilkan_kontak(urut=True)
        elif pilih == 7:
            simpan_data()
        elif pilih == 8:
            muat_data()
        elif pilih == 9:
            print("👋 Terima kasih telah menggunakan program ini!")
            break
        else:
            print("⚠ Pilihan tidak ada!\n")
    except ValueError:
        print("⚠ Masukkan angka saja!\n")
