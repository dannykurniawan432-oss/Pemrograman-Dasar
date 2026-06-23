# operasi logika atau boolean

# not, or, and, xor

# not
print('===NOT===')
a = True
c = not a
print('data a =',a)
print('-----NOT')
print('data c =',c)

print('===OR===')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

print('===AND===')
# AND (jika dua buah nilai true, maka hasil true)
a = False
b = False
c = a and b
print(a,'and',b,'=',c)

a = False
b = True
c = a and b
print(a,'and',b,'=',c)

a = True
b = False
c = a and b
print(a,'and',b,'=',c)

a = True
b = True
c = a and b
print(a,'and',b,'=',c)

print('===XOR===')
# Xor, akan true jika salah satu true, sisanya false
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

