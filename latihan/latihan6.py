kelas = input("masukkan nama kelas :")
jumlah_siswa = int(input("masukkan jumlah siswa dalam kelas :"))

total_nilai = 0
for i in range(jumlah_siswa):
    print("siswa ke-{}".format(i+1))
    nama_siswa = input("masukkan nama siswa :")
    nilai_siswa = int(input("masukkan nilai siswa :"))
    total_nilai += nilai_siswa

rata_rata = total_nilai / jumlah_siswa
print("nama kelas adalah :{}".format(kelas))
print("Rata-rata nilai kelas adalah :{}".format(rata_rata))

if rata_rata < 75:
    status_kelas = "KELAS REMEDIAL"
else:
    status_kelas = "KELAS LULUS"

print("Status kelas :{}".format(status_kelas))