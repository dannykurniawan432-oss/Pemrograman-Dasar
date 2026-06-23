# Input nama mahasiswa
nama_mahasiswa = input("Masukkan nama mahasiswa: ")

# Input jumlah matakuliah
jumlah_matakuliah = int(input("Masukkan jumlah matakuliah: "))

# Inisialisasi variabel
total_ip = 0

# Input data tiap matakuliah
for i in range(jumlah_matakuliah):
    print("\nMatakuliah ke-{}".format(i + 1))
    nama_mk = input("Nama matakuliah: ")
    nilai = float(input("Nilai matakuliah (0-100): "))
    sks = int(input("Jumlah SKS: "))
    
    ip_mk = nilai * sks
    total_ip += ip_mk
    print("IP matakuliah '{}' = {:.2f}".format(nama_mk, ip_mk))

# Hitung IPK
ipk = total_ip / jumlah_matakuliah

# Tampilkan hasil
print("\n===== HASIL PERHITUNGAN =====")
print("Nama Mahasiswa : {}".format(nama_mahasiswa))
print("Jumlah Matakuliah : {}".format(jumlah_matakuliah))
print("Total IP         : {:.2f}".format(total_ip))
print("IPK              : {:.2f}".format(ipk))

# Cek kelulusan
if ipk < 60:
    print("Status           : TIDAK LULUS")
else:
    print("Status           : LULUS")
print("==============================")
