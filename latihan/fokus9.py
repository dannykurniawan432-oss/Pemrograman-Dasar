user = input(str("masukkan nama anda:"))    
pasword = input(str("masukkan password anda:"))
if user == "admin" and pasword == "sayaadmin":
    print("akses diterima, selamat datang", user)
else:
    print("akses ditolak, periksa kembali user dan password anda")

