danny = {"Mady": 8, "Roger": 5, "paul": 5, "Lucy": 7}
print(danny)
dict = {"Ken": 8, "Andrea": 7, "smith": 6}
print(dict)

danny.update(dict)
print(danny)

danny["Roger"] = 8
danny["paul"] = 8
danny["smith"] = 8
print(danny)

for nama, nilai in danny.items():
    if nilai >= 8:
        print (nama, nilai)
