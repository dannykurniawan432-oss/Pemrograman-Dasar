nilai = 57
if nilai > 80:
    print("A")
elif nilai > 65:
    print("B")
elif nilai > 50:
    print("C")
else:
    print("D")

nilai_MK_PD = "A"
kehadiran=80

# penggunaan operator AND
if nilai_MK_PD == "A" and kehadiran==100:
    print("Dapat mengambil MK Basis Data")
else:
    print("Tidak dapat mengambil MK Basis Data")

# penggunaan operator OR
if nilai_MK_PD == "A" or kehadiran==100:
    print("Dapat mengambil MK Basis Data")
else:
    print("Tidak dapat mengambil MK Basis Data")

jumlah_anggota = int(input("Masukan jumlah Anggota:"))
umur_setiap_anggota = int(input("Masukan Umur Setiap Anggota:"))
total_umur = jumlah_anggota*umur_setiap_anggota

if total_umur <= 95:
    print("Tim ini boleh mengikuti lomba")
else:
    print("tim ini tidak boleh mengikuti lomba")





