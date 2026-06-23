# contoh fungsi tanppa parameter
def sapa():
    print("Halo, selamat datang!")
sapa()

# contoh fungsi dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}, selamat datang!")
sapa_nama("Anderson")
sapa_nama("Mady")
sapa_nama("Jame")

# contoh dengan return
def jumlah(a, b):
    return a + b
hasil = jumlah(5, 7)
print(f"Hasil penjumlahan: {hasil}")

def kali(a, b):
    return a * b
hasil_kali = kali(4, 6)
print(f"Hasil perkalian: {hasil_kali}")

# contoh hitung luas lingkaran
def luas_lingkaran(jari_jari):
    phi = 3.14
    luas = phi * jari_jari * jari_jari
    return luas
hasil_luas = luas_lingkaran(10)
print(f"Hasil luas lingkaran: {hasil_luas}")

# contoh hitung keliling lingkaran
def keliling_lingkaran(jari_jari):
    phi = 3.14
    keliling = 2 * phi * jari_jari
    return keliling
hasil_keliling = keliling_lingkaran(10)
print(f"Hasil keliling lingkaran: {hasil_keliling}")

phi = 3.14 
def luas_lingkaran(r):
    luas = phi * r * r
    return luas

def keliling_lingkaran(r):
    keliling = 2 * phi * r
    return keliling   
  
hasil_luas = luas_lingkaran(10)
print(f"Luas lingkaran dengan jari-jari 7: {hasil_luas}")
hasil_keliling = keliling_lingkaran(10)
print(f"Keliling lingkaran dengan jari-jari 7: {hasil_keliling}")