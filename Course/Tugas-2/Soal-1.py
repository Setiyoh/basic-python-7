# Program Kontak
# List Kontak
namaKontak = ["Neko", "Ochie"]
noTelepon = ["08112081075", "08112225478"]

def daftarKontak():  # menampilkan kontak dalam list kontak
    print("Daftar Kontak:")
    for i in range(len(namaKontak)):
        print("Nama: {}".format(namaKontak[i]))
        print("No Telepon: {}".format(noTelepon[i]))

def tambahKontak():  # menambahkan kontak
    namaKontak.append(input("Nama: "))
    noTelepon.append(input("No Telepon: "))
    print("Kontak berhasil ditambahkan")

while True:
    print("Selamat datang!")
    print("--Menu--")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    menu = int(input("Pilih Menu: "))
    if menu == 1:
        daftarKontak()
    elif menu == 2:
        tambahKontak()
    elif menu == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")