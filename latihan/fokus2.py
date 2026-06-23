# kita belajar casting tipe data
# casting : merubah dari satu tipe data ke tipe data lain
# tipe data int, float, str, bool


### integer
print("===integer===")
data_int = 9;
print("data :", data_int, ", bertipe:", type(data_int))

data_float = float(data_int)
print("data :", data_float, ", bertipe:", type(data_float))

data_str = str(data_int)
print("data :", data_str, ", bertipe:", type(data_str))

data_bool = bool(data_int) # akan false jika data_int = 0
print("data :", data_bool, ", bertipe:", type(data_bool))

### float
print("===float===")
data_float = 9.9;     
print("data :", data_float, ", bertipe:", type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
print("data :", data_int, ", bertipe:", type(data_int))

data_str = str(data_float)
print("data :", data_str, ", bertipe:", type(data_str))

data_bool = bool(data_float) # akan false jika data_float = 0.0
print("data :", data_bool, ", bertipe:", type(data_bool))

## boolean
print("===boolean===")              
data_bool = False;
print("data :", data_bool, ", bertipe:", type(data_bool))   
data_int = int(data_bool) # akan 0 jika False, 1 jika True
print("data :", data_int, ", bertipe:", type(data_int))
data_float = float(data_bool) # akan 0.0 jika False, 1.
print("data :", data_float, ", bertipe:", type(data_float))
data_str = str(data_bool) 
print("data :", data_str, ", bertipe:", type(data_str))

### string
print("===string===")           
data_str = "10";
print("data :", data_str, ", bertipe:", type(data_str))
data_int = int(data_str) # harus angka dalam string
print("data :", data_int, ", bertipe:", type(data_int))
data_float = float(data_str) # harus angka dalam string
print("data :", data_float, ", bertipe:", type(data_float))
data_bool = bool(data_str) # akan false jika string kosong ""
print("data :", data_bool, ", bertipe:", type(data_bool))


