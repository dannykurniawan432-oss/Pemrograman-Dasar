def option():
    print ("pilih salah satu dari tiga fungsionalitas di bawah ini:")
    print ("1. menyimpan biodata")
    print ("2. tampilkan semua biodata")
    print ("3. keluar dari program")
    pilihan = int(input("Masukkan pilihan Anda: "))
    return pilihan                      

def simpan_biodata(nama, umur, alamat):
    biodata = {
        "nama": nama,
        "umur": umur,
        "alamat": alamat
    }
    return biodata
def tampilkan_biodata(biodata_list):
    for index, biodata in enumerate(biodata_list):
        print(f"Biodata {index + 1}:")
        print(f"Nama: {biodata['nama']}")
        print(f"Umur: {biodata['umur']}")
        print(f"Alamat: {biodata['alamat']}")
        print("-----------------------")
biodata_list = []
pilihan = 0
while(pilihan<3):
    pilihan = option()
    if pilihan == 3 | pilihan ==0:
        break
    elif pilihan ==1:
        nama = input("Masukkan Nama: ")
        umur = input("Masukkan Umur: ")
        alamat = input("Masukkan Alamat: ")
        biodata = simpan_biodata(nama, umur, alamat)
        biodata_list.append(biodata)
        print("Biodata berhasil disimpan!")
    elif pilihan == 2:
        if len(biodata_list) == 0:
            print("Tidak ada biodata yang tersimpan.")
        else:
            tampilkan_biodata(biodata_list)
    else:
        print("Pilihan tidak valid! silakan masukkan 1, 2, atau 3.")
        