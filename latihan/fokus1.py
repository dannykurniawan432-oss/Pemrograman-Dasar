# belajar tipe data
# a = 25, a adalah variabel dengan nilai 25

# tipe data : Angka satuan (integer)
data_integer = 1
print(type(data_integer))
print("- data :", data_integer, ", bertipe:", type(data_integer))

# tipe data : Angka dengan koma (float)
data_float = 1.5
print(type(data_float))
print("- data :", data_float, ", bertipe:", type(data_float))

# tipe data : Kumpulan karakter (string)
data_string = "Hello, World!"
print(type(data_string))
print("- data :", data_string, ", bertipe:", type(data_string))

# tipe data : biner true/false (boolean)
data_boolean = True
print(type(data_boolean))
print("- data :", data_boolean, ", bertipe:", type(data_boolean))

# tipe data khusus
# tipe data : bilangan kompleks (complex)   
data_complex = complex(5, 6)
print(type(data_complex))
print("- data :", data_complex, ", bertipe:", type(data_complex))

#3 tipe data dari bahasa C
from ctypes import c_double, c_char
data_c_double = c_double(10.5)
data_c_char = c_char(b'A')
print(type(data_c_double))
print("- data :", data_c_double.value, ", bertipe:", type(data_c_double))
print(type(data_c_char))
print("- data :", data_c_char.value, ", bertipe:", type(data_c_char))
