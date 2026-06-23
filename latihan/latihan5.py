a = range(1,8,+3) #melakukan incremen dengan penambahan 3
print("Berikut isi variable a : {}".format(list(a)))

b = range(20,2,-2) #melakukan dekrement dengan pengurangan 2
print("Berikut isi variable b : {}".format(list(b)))

for i in range(10,2,-2):
    print("isi i adalah {} ".format(i))

for i, item in enumerate(range(10,2,-2)):
    print("isi i pada index {} adalah {}".format(i,item))

for i in range(0,5):
    for j in range(0,i+1):
        print("*", end="")
    print()

suhu = 0
while suhu < 100:
    print(suhu)
    suhu += 40

angka = int(input("masukkan angka faktorial : "))
hasil = 1
for i in range (1,angka+1):
    hasil = hasil * i
print(" Hasil Faktorial angka {} adalah {}".format(angka,hasil))

angka = int(input("masukkan angka maks : "))
hasil = 0
for i in range (0,angka+1):
    hasil = hasil + i
print(" Hasil angka maks {} adalah {}".format(angka,hasil))