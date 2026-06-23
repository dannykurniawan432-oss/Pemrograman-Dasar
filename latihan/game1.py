import random

print("=== Permainan Tebak Angka ===")
angka_rahasia = random.randint(1, 20)
percobaan = 0

while True:
    tebakan = input("Tebak angka antara 1-20: ")
    if not tebakan.isdigit():
        print("Masukkan angka yang valid!")
        continue

    tebakan = int(tebakan)
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"🎉 Benar! Angkanya {angka_rahasia}. Kamu menebak dalam {percobaan} kali.")
        break
