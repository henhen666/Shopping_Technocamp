# print("Selamat datang di Technocamp Quiz Application!")
# s = str(input("Siap mengerjakan ujian?: "))
# if s == "Yes":
#     print()
# while s == "No":
#     print("Silakan coba nanti!")
#     s = str(input("Siap mengerjakan ujian?: "))


# print("1. 10 x 5 = ")
# s1 = int(input("Jawaban: "))
# if s1 == 50:
#     print("Jawaban anda benar!")
# else:
#     print("Jawaban anda salah!")
# print("2. Ibu kota dari Provinsi Sumatera Utara adalah: ")
# s1 = str(input("Jawaban: "))
# if s1 == "Medan":
#     print("Jawaban anda benar!")
# elif s1 == "medan":
#     print("Jawaban anda benar!")
# else:
#     print("Jawaban anda salah!")
# print("3. Akar kuadrat dari 144 adalah: ")
# s1 = int(input("Jawaban: "))
# if s1 == 12:
#     print("Jawaban anda benar!")
# else:
#     print("Jawaban anda salah!")
# print("Presiden terpilih Amerika Serikat sekarang adalah: ")
# s1 = str(input("Jawaban: "))
# if s1 == "Joe Biden":
#     print("Jawaban anda benar!")
# elif s1 == "joe biden":
#     print("Jawaban anda benar!")
# else:
#     print("Jawaban anda salah!")
# print("Jika x + 2 = -22, berapakah nilai x?")
# s1 = int(input("Jawaban: "))
# if s1 == -24:
#     print("Jawaban anda benar!")
# else:
#     print("Jawaban anda salah!")

#simple online shop
print("Selamat datang di Technocamp Online Shop!")
print("Silakan melakukkan login terlebih dahulu.")
user = str(input("Username: "))
pswd = str(input("Password: "))
print(f"Anda login sebagai {user}!")
print()
print("Daftar belanja: \n Kosong")
print()
print("Silakan pilih barang yang ingin dibeli!")
arr = ["1. Meja Rp5000", "2. Alat tulis Rp4000", "3. Kursi Rp3000", "4. Kitchen Set Rp7000"]
print("Cek keranjang")
a = int(input("Pilihan user: "))
if a == 1:
    print(arr[0])
    jmlh = int(input("Banyak meja yang ingin ditambahkan: "))
    print(f"{jmlh} meja berhasil ditambahkan!")
elif a == 2:
    print(arr[1])
    jmlh = int(input("Banyaknya Alat tulis yang ingin dibeli: "))
    print(f"{jmlh} alat tulis berhasil ditambahkan!")
elif a == 3:
    print(arr[2])
    jmlh = int(input("Banyaknya kursi yang ingin dibeli: "))
    print(f"{jmlh} kursi berhasil ditambahkan!")
elif a == 4:
    print(arr[3])
    jmlh = int(input("Banyaknya kitchen set yang ingin dibeli: "))
    print(f"{jmlh} kitchen set berhasil ditambahkan!")
while a < 1:
    print("Barang tidak tersedia! Coba yang lain!")
    a = int(input("Pilihan user: "))
while a > 4:
    print("Barang tidak tersedia! Coba yang lain!")
    a = int(input("Pilihan user: "))
arr1 = []
arr1.append(a)

x = str(input("Barang apalagi yang ingin ditambah ke keranjang? (Tidak ada/ada): "))
if x == "Tidak ada":
    print("Pembelian selesai!")
elif x == "ada":
    a = int(input("Pilihan user: "))

