# operasi komperasi

# setiap hasil dari operasi komperasi adalah

# >, <, >=, <=, ==, !=, is, is not

a = 32
b = 2

# lebih besar dari >
print('===lebih besar dari(>)')
hasil = a > 31
print (a,'>',31,'=',hasil)
hasil = b > 31
print (b,'>',31,'=',hasil)
hasil = b > 32
print (b,'>',32,'=',hasil)

# lebih kurang dari <
print('===kurang dari(<)')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print('=== lebih dari sama dengan (>=)')
hasil = a >= 3
print(a, '>=', 3 ,'=', hasil)
hasil = b >= 3
print(b, '>=', 3 ,'=', hasil)
hasil = b >= 2
print(b, '>=', 2 ,'=', hasil)

# kurang dari sama dengan >=
print('=== lebih dari sama dengan (<=)')
hasil = a <= 3
print(a, '<=', 3 ,'=', hasil)
hasil = b <= 3
print(b, '<=', 3 ,'=', hasil)
hasil = b <= 2
print(b, '<=', 2 ,'=', hasil)

# sama denagan (==)
print('===sama dengan (==)')
hasil = a == 32
print(a,'==',32,'=', hasil)
hasil = b == 32
print(b,'==',32,'=', hasil)

# tidak sama denagan (!=)
print('=== tidak sama dengan (!=)')
hasil = a != 32
print(a,'!=',32,'=', hasil)
hasil = b != 32
print(b,'!=',32,'=', hasil)

# 'is' sebagai komparasi object identity
print('=== object identity (is)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id =', hex(id(x)))
print('nilai y =',x,',id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# 'is' sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id =', hex(id(x)))
print('nilai y =',x,',id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id =', hex(id(x)))
print('nilai y =',x,',id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

# 'is' sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id =', hex(id(x)))
print('nilai y =',x,',id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)