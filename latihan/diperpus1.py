# Nama file : input_string.py
from __future__ import print_function

def main():
    # membuat prompt untuk tipe data string
    nama = input("masukkan nama anda : ")

    #membuat prompt untuk tipe data karakter
    karakter = input ("masukkan sebuah karakter : ")

    # menampilkan nilai variabel 
    print ("Hallo", nama, "apa kabar?")
    print ("karakter yang dimasukkan: '", karakter, "'")

if __name__ == "__main__":
    main()