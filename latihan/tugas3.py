
nama = input("masukkan nama anda :")
jumlah_mk = int(input("masukkan jumlah mata kuliah yang diambil :"))

total_nilai = 0

for i in range(jumlah_mk):
    print("mata kuliah ke-{}".format(i+1))
    nama_mk = input("masukkan nama mata kuliah :")
    nilai = int(input("masukkan nilai mata kuliah :"))
    total_nilai += nilai

ipk = total_nilai / int(jumlah_mk)

if ipk < 60:
    status = "TIDAK LULUS"
else:
    status = "LULUS"

print("nama mahasiswa adalah :{}".format(nama))
print("IPK :",(ipk))
print("Status :",(status))
