hari_pertama = ("lukman", "andi", "soleh", "putri")
hari_kedua = ("soleh", "putri", "andi")
gabungan_hari = hari_pertama + hari_kedua

print(hari_pertama)
print(hari_kedua)
print(hari_pertama[2])
print(gabungan_hari)
print(gabungan_hari.count("putri"))
print("lukman" in hari_kedua)
print("andi" in gabungan_hari)
for data in gabungan_hari:
    print(data)
