# episode latihan logika dan komperasi

# membuat gabungan area rentang dari angka

inputuser = float(input("masukan angka yang bernilai \nkurang dari 3 \natau \nlebih dari 10:"))
# memeriksa angka kurang dari 3
iskurangdari = (inputuser < 3)
print(iskurangdari)
#memeriksa angka lebioh dari 10
islebihdari = (inputuser > 10)
print("lebih dari 10=", islebihdari)

iscorrect = iskurangdari or islebihdari
print ("angka yang anda masukan:", iscorrect)
