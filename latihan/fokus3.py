# input dari user

print("=== Input dari user ===")
data = input("Masukkan data: ") # input selalu mengembalikan string
print("data :", data, ", bertipe:", type(data))

# jika ingin mengambil tipe data selain string, harus di-casting terlebih dahulu
data_int = int(input("Masukkan data integer: "))
print("data :", data_int, ", bertipe:", type(data_int))
data_float = float(input("Masukkan data float: "))
print("data :", data_float, ", bertipe:", type(data_float))
data_bool = bool(int(input("Masukkan data boolean (0/1): ")))
print("data :", data_bool, ", bertipe:", type(data_bool))

