# Program Kasir Sederhana

jumlah_variasi_barang = int(input("masukkan variasi barang yang akan dibeli :"))
total_harga = 0

for i in range(jumlah_variasi_barang):

    nama_barang = str(input("masukkan nama barang :"))
    harga_barang = int(input("masukkan harga barang :"))
    jumlah_barang = int(input("masukkan jumlah barang :"))

    total_harga = total_harga + (harga_barang * jumlah_barang)
bayar = 0
if total_harga > 500000:
    bayar = total_harga - (10/100 * total_harga)
else :
    bayar = total_harga
print("uang yang harus dibayar adalah : rp.{}".format(bayar))


