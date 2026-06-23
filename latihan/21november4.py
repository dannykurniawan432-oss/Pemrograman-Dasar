def option():
    print ("pilih salah satu dari tiga fungsionalitas di bawah ini:")
    print ("1. Konversi jam ke menit")
    print ("2. Konversi menit ke detik")
    print ("3. keluar")
    pilihan = int(input("Masukkan pilihan Anda: "))
    return pilihan

def jam_ke_menit(jam):
    menit = jam * 60
    return menit

def menit_ke_detik(menit):
    detik = menit * 60
    return detik
pilihan = 0

while(pilihan<3):
    pilihan = option()
    if pilihan == 3:
        break
    elif pilihan ==1:
        jam = float(input("Masukkan jumlah jam: "))
        hasil_menit = jam_ke_menit(jam)
        print(f"{jam} jam adalah {hasil_menit} menit.")
    elif pilihan == 2:
        menit = float(input("Masukkan jumlah menit: "))
        hasil_detik = menit_ke_detik(menit)
        print(f"{menit} menit adalah {hasil_detik} detik.")
    else:
        print("Pilihan tidak valid! silakan masukkan 1, 2, atau 3.")

        