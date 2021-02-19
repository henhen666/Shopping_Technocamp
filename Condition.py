#genap atau ganjil
a = int(input ("Masukkan bilangan: "))
if (a % 2 == 0):
    if(a >= 1):
        print(f"{a} adalah bilangan positif genap")
if(a % 2 != 0):
    if(a < 0):
        print(f"{a} adalah bilangan negatif ganjil ")
if(a % 2 == 0) & (a < 0):
    print(f"{a} adalah bilangan negatif genap")
if(a % 2 != 0) & (a > 0):
    print(f"{a} adalah bilangan positif ganjil")

# #konversi nilai
x = int(input("Masukkan Nilai Akhir: "))
if (x >= 80):
    if (x <= 100):
        print("Indeks: A")
if (x >= 73):
    if(x <= 79):
        print("Indeks: AB")
if(x >= 65):
    if(x <= 72):
        print("Indeks: B")
if( x >= 57):
    if(x <= 64):
        print("Indeks: BC")
if(x >= 50):
    if(x <= 56):
        print("Indeks: C")
if(x >= 35):
    if(x <= 49):
        print("Indeks: D")
if(x >= 0):
    if(x <= 34):
        print("Indeks: E")

bil = int(input("Masukkan bilangan: "))
if(bil % 6 == 0):
    print(f"{bil} adalah kelipatan 6")
else:
    print(f"{bil} bukan kelipatan 6")

#akar kuadrat
a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
c = float(input("Masukkan c: "))
determinan = b**2 - 4*a*c
if(determinan < 0):
    print("Akar-akarnya tidak ada")
else:
    x1 = (-b + (determinan**(1/2))) / 2*a
    x2 = (-b - (determinan**(1/2))) / 2*a
    if (x1 == x2):
        print(f"Akarnya cuma satu, yaitu: {x1}")
    else:
        print(f"Akarnya ada dua {x1}, {x2}")