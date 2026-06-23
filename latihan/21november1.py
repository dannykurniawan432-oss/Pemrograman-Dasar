phi = 3.14 
def luas_lingkaran(r):
    luas = phi * r * r
    return luas

def keliling_lingkaran(r):
    keliling = phi * (r*2)
    return keliling 

hitung_luas = luas_lingkaran(10)
print("Luas lingkaran adalah {}".format(hitung_luas))

hitung_keliling = keliling_lingkaran(50)
print("keliling lingkaran adalah {}".format(hitung_keliling))


def volume_balok(p, l, t):
    volume = p * l * t
    return volume
hitung_volume = volume_balok(13, 16, 30)
print("Volume balok adalah {}".format(hitung_volume))

def luas_persegi(s):
    luas = s * s
    return luas
hitung_luas_persegi = luas_persegi(7)
print("luas persegi adalah {}".format(hitung_luas_persegi))

def keliling_persegi(s):
    keliling = 4 * s
    return keliling
hitung_keliling_persegi = keliling_persegi(7)
print("keliling persegi adalah {}".format(hitung_keliling_persegi))

def luas_permukaan_kubus(s):
    luas = 6 * s * s
    return luas
hitung_luas = luas_permukaan_kubus(12)
print("luas permukaan kubus adalah {}".format(hitung_luas))

def volume_kubus(s):
    volume = s * s * s
    return volume
hitung_volume = volume_kubus(12)
print("volume kubus adalah {}".format(hitung_volume))