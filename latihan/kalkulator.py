# Kalkulator Sederhana
print("=== Kalkulator Sederhana ===")

# Input angka pertama
angka1 = float(input("Masukkan angka pertama: "))

# Input operator
operator = input("Pilih operator (+, -, *, /): ")

# Input angka kedua
angka2 = float(input("Masukkan angka kedua: "))

# Operasi
if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error! Tidak bisa dibagi 0."
else:
    hasil = "Operator tidak valid!"

# Tampilkan hasil
print("Hasil:", hasil)
