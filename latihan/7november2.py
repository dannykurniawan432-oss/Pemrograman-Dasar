hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}
gabungan_hari = hari_pertama.union(hari_kedua)
print(gabungan_hari)

hari_kedua.add("keju")
print(hari_kedua)

gabungan_hari = hari_pertama.intersection(hari_kedua)
print(gabungan_hari)

gabungan_hari = hari_pertama.difference(hari_kedua)
print(gabungan_hari)

hari_pertama.discard("garam")
print(hari_pertama)

tidak_ada =hari_kedua.difference(hari_pertama)
print(tidak_ada)

bukan_ada = hari_pertama.symmetric_difference(hari_kedua)
print(bukan_ada)

print("hari_pertama")
for data in hari_pertama:
    print(data)
print("hari_kedua")
for data in hari_kedua:
    print(data)