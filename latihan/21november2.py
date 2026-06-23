def option():
    print ("pilih salah satu dari tiga fungsionalitas di bawah ini:")
    print ("1. Mencari luas persegi panjang")
    print ("2. Mencari keliling persegi panjang")
    print ("3. keluar dari program")
    pilihan = int(input("Masukkan pilihan Anda: "))
    return pilihan
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas
def keliling_persegi_panjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    return keliling
pilihan = 0

while(pilihan<3):
    pilihan = option()
    if pilihan == 3:
        break
    elif pilihan ==1:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        hasil_luas = luas_persegi_panjang(panjang, lebar)
        print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {hasil_luas}.")
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        hasil_keliling = keliling_persegi_panjang(panjang, lebar)
        print(f"Keliling persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {hasil_keliling}.")
    else:
        print("Pilihan tidak valid! silakan masukkan 1, 2, atau 3.")