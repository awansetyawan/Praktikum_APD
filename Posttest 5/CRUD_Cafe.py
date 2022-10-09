# Login Administrasi
 
admin = 'admin'
password_admin = 'admin'

# Login Pembeli

konsumen = 'kasir'
password_konsumen = 'kasir'

# List Menu

list_pesanan = {}
 
menu_makan ={"kentang"       : 13000,
            "tahu krispy"    : 13000,
            "roti bakar"     : 15000,
            "hamburger"      : 15000,
            "pisang cokelat" : 12000,
            "pisang keju"    : 12000,
            "sosis bakar"    : 15000,
            "nugget ayam"    : 15000}

menu_minum ={"kopi caramel"  : 20000,
            "kopi latte"     : 20000,
            "cappucino"      : 15000,
            "moccacino"      : 15000,
            "kopi robusta"   : 12000,
            "kopi tubruk"    : 12000,
            "milkshake"      : 10000,
            "teh tarik"      : 10000,}


# Fungsi-Fungsi Kasir

def makanan () :
    menu_makan
    for data, nilai in menu_makan.items() :
        print(data,'\t> Rp.', nilai)

    print()
    print (52*"=")
    print (21*"-", "Pesanan", 22*"-")
    print (52*"=")
    while True :
        try:
            i = input("Masukkan Nama Menu                  = ")
            j = menu_makan[i]
            a = int(input("Masukkan Jumlah Pesanan             = "))
            b = (input("Hari                                = "))
            jumlah = j * a
            if b in ("senin", "selasa", "rabu", "kamis", "Jumat") :
                if a >= 2 :
                    persentase1 = 10/100
                    persentase2 = 5/100
                    diskon1 = jumlah * persentase1
                    diskon2 = jumlah * persentase2 

                    print (52*"=")
                    print ("Diskon Weekdays 10 % + Diskon Beli 2")
                    x = diskon1 + (diskon2 * (1 - persentase1))
                    y = (int(jumlah - x))
                    print ("Total Belanja + Diskon   = ", 'Rp.', y)
                    print (52*"=")

                    bayar = input("Bayar Pakai E-Money ? [y/t] : ")
                    if bayar == "y" :
                        hasil = y * (5/100)
                        pembayaran = (int(y - hasil))
                        print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                        print (52*"=")
                        
                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, pembayaran]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, pembayaran]

                    else :
                        print ("Total Bayar              = ", 'Rp.', y)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, y]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, y]

                else :
                    persentase = 10/100
                    x = jumlah * persentase
                    y = (int(jumlah - x))

                    print (52*"=")
                    print ("Diskon Weekdays 10 %")
                    print ("Total Belanja + Diskon   = ", 'Rp.', y)
                    print (52*"=")

                    bayar = input("Bayar Pakai E-Money ? [y/t] : ")
                    if bayar == "y" :
                        hasil = y * (5/100)
                        pembayaran = (int(y - hasil))
                        print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, pembayaran]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, pembayaran]

                    else :
                        print ("Total Bayar              = ", 'Rp.', y)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, y]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, y]
                break


            elif b in ("sabtu", "minggu"):
                if a >= 2 :
                    persentase = 5/100
                    diskon = jumlah * persentase

                    print (52*"=")
                    print ("Diskon Weekend 5 % + Diskon Beli 2")
                    x = diskon + (diskon * (1 - persentase))
                    y = (int(jumlah - x))
                    print ("Total Belanja + Diskon   = ", 'Rp.', y)
                    print (52*"=")

                    bayar = input("Bayar Pakai E-Money ? [y/t] : ")
                    if bayar == "y" :
                        hasil = y * (5/100)
                        pembayaran = (int(y - hasil))
                        print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, pembayaran]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, pembayaran]

                    else :
                        print ("Total Bayar              = ", 'Rp.', y)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, y]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, y]

                else :
                    persentase = 5/100
                    x = jumlah * persentase
                    y = (int(jumlah - x))

                    print (52*"=")
                    print ("Diskon Weekend 5 %")
                    print ("Total Belanja + Diskon   = ", 'Rp.', y)
                    print (52*"=")

                    bayar = input("Bayar Pakai E-Money ? [y/t] : ")
                    if bayar == "y" :
                        hasil = y * (5/100)
                        pembayaran = (int(y - hasil))
                        print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, pembayaran]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, pembayaran]

                    else :
                        print ("Total Bayar              = ", 'Rp.', y)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, y]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, y]
                break
            
            else:
                print()
                print("Salah input hari, coba lagi")
                print()

        except ValueError:
            print()
            print('Salah memasukan tipe data (angka)')
            print()
        except KeyError :
            print()
            print('Data menu tidak ada')
            print()
        print (52*"=")

def minuman ():
    menu_minum
    for data, nilai in menu_minum.items():
        print(data,'\t> Rp.', nilai)

    print()
    print (52*"=")
    print (21*"-", "Pesanan", 22*"-")
    print (52*"=")
    while True:
        try:
            i = input("Masukkan Nama Menu                  = ")
            j = menu_minum[i]
            a = int(input("Masukkan Jumlah Pesanan             = "))
            b = (input("Hari                                = "))
            jumlah = j * a
            if b in ("senin", "selasa", "rabu", "kamis", "Jumat") :
                if a >= 3 :
                    persentase = 10/100
                    diskon = jumlah * persentase

                    print (52*"=")
                    print ("Diskon Weekdays 10 % + Diskon Beli 3")
                    x = diskon + (diskon * (1 - persentase))
                    y = (int(jumlah - x))
                    print ("Total Belanja + Diskon   = ", 'Rp.', y)
                    print (52*"=")

                    bayar = input("Bayar Pakai E-Money ? [y/t] : ")
                    if bayar == "y" :
                        hasil = y * (5/100)
                        pembayaran = (int(y - hasil))
                        print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, pembayaran]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, pembayaran]

                    else :
                        print ("Total Bayar              = ", 'Rp.', y)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, y]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, y]

                else :
                    persentase = 10/100
                    x = jumlah * persentase
                    y = (int(jumlah - x))

                    print (52*"=")
                    print ("Diskon Weekdays 10 %")
                    print ("Total Belanja + Diskon   = ", 'Rp.', y)
                    print (52*"=")

                    bayar = input("Bayar Pakai E-Money ? [y/t] : ")
                    if bayar == "y" :
                        hasil = y * (5/100)
                        pembayaran = (int(y - hasil))
                        print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, pembayaran]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, pembayaran]

                    else :
                        print ("Total Bayar              = ", 'Rp.', y)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, y]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, y]
                break

            elif b in ("sabtu", "minggu"):
                if a >= 3 :
                    persentase1 = 5/100
                    persentase2 = 10/100
                    diskon1 = jumlah * persentase1
                    diskon2 = jumlah * persentase2

                    print (52*"=") 
                    print ("Diskon Weekend 5 % + Diskon Beli 3")
                    x = diskon1 + (diskon2 * (1 - persentase1))
                    y = (int(jumlah - x))
                    print ("Total Belanja + Diskon   = ", 'Rp.', y)
                    print (52*"=")

                    bayar = input("Bayar Pakai E-Money ? [y/t] : ")
                    if bayar == "y" :
                        hasil = y * (5/100)
                        pembayaran = (int(y - hasil))
                        print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, pembayaran]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, pembayaran]

                    else :
                        print ("Total Bayar              = ", 'Rp.', y)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, y]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, y]

                else :
                    persentase = 5/100
                    x = jumlah * persentase
                    y = (int(jumlah - x))

                    print (52*"=")
                    print ("Diskon Weekend 5 %")
                    print ("Total Belanja + Diskon   = ", 'Rp.', y)
                    print (52*"=")

                    bayar = input("Bayar Pakai E-Money ? [y/t] : ")
                    if bayar == "y" :
                        hasil = y * (5/100)
                        pembayaran = (int(y - hasil))
                        print ("Total Bayar + Diskon 5 % = ", 'Rp.',pembayaran)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, pembayaran]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, pembayaran]

                    else :
                        print ("Total Bayar              = ", 'Rp.', y)
                        print (52*"=")

                        if len(list_pesanan) <= 0 :
                            list_pesanan[i] = [j, jumlah, y, y]
                        else:
                            del list_pesanan[i]
                            list_pesanan[i] = [j, jumlah, y, y]
                break

            else:
                print()
                print("Salah input hari, coba lagi")
                print()
        
        except ValueError:
            print()
            print('Salah memasukan tipe data (angka)')
            print()
        except KeyError :
            print()
            print('Data menu tidak ada')
            print()
        print (52*"=")

def lihat():
    print("Peringatan : \nMemasukkan menu baru akan menghapus struk pesanan yang lama")
    print()
    print("==========================================================================================")
    print("|-------------------------------------Daftar Harga Pesanan-------------------------------|")
    if len(list_pesanan) <= 0:  
        print("==========================================================================================")
        print("|---------------------------------------Tidak Ada Pesanan--------------------------------|")
        print("==========================================================================================")
    else:
        no = 0
        for data in list_pesanan.items():
            no += 1
            print(90*"=")
            print("| {1:^14} | {2:^19} | {3:^17} | {4:^8} | {5:^12} |".format("", "Nama", "Harga", "Total Harga", "Total Diskon", "Pembayaran")) 
            print(90*"=")
            print(f"| {data[0]:^14} | Rp.{data[1][0]:^16} | Rp.{data[1][1]:^14} | Rp.{data[1][2]:^9} | Rp.{data[1][3]:^9} |")
            print(90*"=")

def diskon () :
    print (36*"=")
    print (14*"-", "Diskon", 14*"-")
    print (36*"=")
    print ("[Diskon] \n1. Membeli 3 Minuman   > 10% \n2. Membeli 2 Makanan   > 5% \n3. Bayar Lewat E-money > 5% \n4. Weekend             > 5% \n5. Weekdays            > 10%")

# Program Kasir

def kasir() :
    while True :
        print()
        print (38*"=")
        print (11*"-", "Selamat Datang", 11*"-")
        print (38*"=")
        print (16*"-", "Menu", 16*"-")
        print (38*"=")
        print ("[1] Makanan \n[2] Minuman \n[3] Diskon \n[4] Struk Pesanan \n[0] Exit")
        x = input('Masukkan Menu [1,2,3,4,0] : ')
        if x == "1" :
            list_pesanan.clear()
            menu_makan
            print()
            print (11*"-", "Menu Makanan", 11*"-")
            print()
            for data, nilai in menu_makan.items() :
                print(data,'\t> Rp.', nilai)

            print (42*"=")
            tanya = input("Apakah ingin memesan ? [ya/tidak] : ")
            print (42*"=")
            if tanya == 'ya':
                print()
                print (11*"-", "Menu Makanan", 11*"-")
                print()
                makanan()
            else:
                False
        elif x == "2" :
            list_pesanan.clear()
            menu_minum
            print()
            print (11*"-", "Menu Makanan", 11*"-")
            print()
            for data, nilai in menu_minum.items() :
                print(data,'\t> Rp.', nilai)

            print (42*"=")
            tanya = input("Apakah ingin memesan ? [ya/tidak] : ")
            print (42*"=")
            if tanya == 'ya':
                print()
                print (11*"-", "Menu Makanan", 11*"-")
                print()
                minuman()
            else:
                False
        elif x == "3" :
            print()
            diskon()
        elif x == "4" :
            print()
            lihat()
        elif x == "0":
            print (38*"=")
            print(3*"-", "Terima Kasih Telah Berkunjung", 4*"-")
            print (38*"=")
            break
        else:
            print("Salah Masukkan Angka \nSilahkan Masukkan Angka Dengan Benar")

# CRUD

def tambah():
    print()
    print (38*"=")
    print (10*"-", "Tambah Data Menu", 10*"-")
    print (38*"=")
    print ("[1] Makanan \n[2] Minuman")
    x = input('Masukkan Menu [1 atau 2] : ')
    if x == '1':
        menu_makan
        print()
        print (61*"=")
        print (25*"-", "Data Menu", 25*"-")
        print (61*"=")
        print()
        for data, nilai in menu_makan.items() :
            print(data,'\t >>', nilai)
        while True:
            try:
                print()
                print (61*"=")
                print (18*"-", "Silahkan Tambahkan Data", 18*"-")
                print (61*"=")
                nama = (input("Masukkan Nama Menu Baru = "))
                harga = int(input("Masukkan Harga          = "))
                menu_makan[nama] = harga
                print (61*"=")
                print (22*"-", "Data Ditambahkan", 21*"-")
                print (61*"=")
                break
            except ValueError:
                print()
                print('Data harga salah !!!')
                print('Mohon diulang dan masukkan dalam bentuk angka')

    elif x == '2':
        menu_minum
        print()
        print (61*"=")
        print (25*"-", "Data Menu", 25*"-")
        print (61*"=")
        print()
        for data, nilai in menu_minum.items() :
            print(data,'\t >>', nilai)
        while True:
            try:
                print()
                print (61*"=")
                print (18*"-", "Silahkan Tambahkan Data", 18*"-")
                print (61*"=")
                nama = (input("Masukkan Nama Menu Baru = "))
                harga = int(input("Masukkan Harga          = "))
                menu_minum[nama] = harga
                print (61*"=")
                print (22*"-", "Data Ditambahkan", 21*"-")
                print (61*"=")
                break
            except ValueError:
                print()
                print('Data harga salah !!!')
                print('Mohon diulang dan masukkan dalam bentuk angka')

    else:
        print()
        print(8*"-", "Salah Masukkan Angka", 8*"-")
        print("-Silahkan Masukkan Angka Dengan Benar-")

def hapus():
    print()
    print (38*"=")
    print (11*"-", "Hapus Data Menu", 10*"-")
    print (38*"=")
    print ("[1] Makanan \n[2] Minuman")
    x = input('Masukkan Menu [1 atau 2] : ')
    if x == '1':
        menu_makan
        print()
        print (65*"=")
        print (22*"-", "Silahkan Hapus Data", 22*"-")
        print (65*"=")

        for data, nilai in menu_makan.items() :
            print(data,'\t >>', nilai)
        print()
        while True :
            try:
                del menu_makan[input("Masukkan Nama Menu Yang Ingin Dihapus = ")]
                print (65*"=")
                print (25*"-", "Data Di Hapus", 25*"-")
                print (65*"=")
                break
            except KeyError :
                print()
                print('Data menu tidak ada')
                print()

    elif x == '2':
        menu_minum
        print()
        print (65*"=")
        print (22*"-", "Silahkan Hapus Data", 22*"-")
        print (65*"=")

        for data, nilai in menu_minum.items() :
            print(data,'\t >>', nilai)
        print()
        while True:
            try:
                del menu_minum[input("Masukkan Nama Menu Yang Ingin Dihapus = ")]
                print (65*"=")
                print (25*"-", "Data Di Hapus", 25*"-")
                print (65*"=")
                break
            except KeyError :
                print()
                print('Data menu tidak ada')
                print()
    
    else:
        print()
        print(8*"-", "Salah Masukkan Angka", 8*"-")
        print("-Silahkan Masukkan Angka Dengan Benar-")

def edit():
    print()
    print (38*"=")
    print (11*"-", "Ubah Data Menu", 11*"-")
    print (38*"=")
    print ("[1] Makanan \n[2] Minuman")
    x = input('Masukkan Menu [1 atau 2] : ')

    if x == '1':
        print()
        print (65*"=")
        print (22*"-", "Silahkan Ubah Harga", 22*"-")
        print (65*"=")

        for data, nilai in menu_makan.items():
            print(data,'\t >>', nilai)
        print()

        while True :
            try:
                menu = input("Nama Menu Yang Ingin Diubah = ")
                harga = int(input("Masukkan Harga Baru         = "))
                menu_makan[menu] = harga
                print (65*"=")
                print (25*"-", "Harga Di Ubah", 25*"-")
                print (65*"=")
                break
            except ValueError:
                print()
                print('Data inputan salah !!!')
                print('Mohon diulang dan masukkan dalam bentuk angka')
                print()

    elif x == '2':
        print()
        print (65*"=")
        print (22*"-", "Silahkan Ubah Harga", 22*"-")
        print (65*"=")

        for data, nilai in menu_minum.items():
            print(data,'\t >>', nilai)
        print()

        while True :
            try:
                menu = input("Nama Menu Yang Ingin Diubah = ")
                harga = int(input("Masukkan Harga Baru         = "))
                menu_minum[menu] = harga
                print (65*"=")
                print (25*"-", "Harga Di Ubah", 25*"-")
                print (65*"=")
                break
            except ValueError:
                print()
                print('Data inputan salah !!!')
                print('Mohon diulang dan masukkan dalam bentuk angka')
                print()
    
    else:
        print()
        print(8*"-", "Salah Masukkan Angka", 8*"-")
        print("-Silahkan Masukkan Angka Dengan Benar-")

def tampilkan():
    print()
    print (38*"=")
    print (14*"-", "Data Menu", 13*"-")
    print (38*"=")
    print ("[1] Makanan \n[2] Minuman")
    x = input('Masukkan Menu [1 atau 2] : ')

    if x == '1':
        menu_makan
        print()
        print (38*"=")
        print (12*"-", "Menu Makanan", 12*"-")
        print (38*"=")

        for data, nilai in menu_makan.items() :
            print(data,'\t >>', nilai)
    
    elif x == '2':
        menu_minum
        print()
        print (38*"=")
        print (12*"-", "Menu Minuman", 12*"-")
        print (38*"=")

        for data, nilai in menu_minum.items() :
            print(data,'\t >>', nilai)
    
    else:
        print()
        print(8*"-", "Salah Masukkan Angka", 8*"-")
        print("-Silahkan Masukkan Angka Dengan Benar-")

# Program Admin

def edit_menu() :

    while True :
        print()
        print (38*"=")
        print (8*"-", "Selamat Datang Admin", 8*"-")
        print (38*"=")
        print (9*"-", "DATABASE MENU CAFE", 9*"-")
        print (38*"=")
        print ("[1] Tambah Data Menu \n[2] Lihat Data \n[3] Ubah Data Menu \n[4] Hapus Data Menu \n[0] Exit")
        x = input('Masukkan Menu [1,2,3,4,0] : ')
        if x == '1' :
            tambah()
        elif x == '2' :
            tampilkan()
        elif x == '3' :
            edit()
        elif x == '4' :
            hapus()
        elif x == '0' :
            print (38*"=")
            print (14*"-", "Bye Admin", 13*"-")
            print (38*"=")
            break
        else :
            print()
            print(8*"-", "Salah Masukkan Angka", 8*"-")
            print("-Silahkan Masukkan Angka Dengan Benar-")

# Program Utama

while True :
    print()
    print (38*"=")
    print (11*"-", "Selamat Datang", 11*"-")
    print (38*"=")
    print (11*"-", "Silahkan Login", 11*"-")
    print (38*"=")
    print ("[1] Login \n[0] Exit")
    x = input('Masukkan Menu [1 atau 0] : ')
    if x == '1' :
        user = (input("Masukkan Username = "))
        pw   = (input("Masukkan Password = "))
        if user == admin and pw == password_admin :
            edit_menu()
        elif user == konsumen and pw == password_konsumen :
            kasir()
        else:
            print (38*"=")
            print (5*"-", "Username atau Password Salah", 4*"-")
            print (38*"=")
    elif x == '0' :
        print()
        print (8*"-", "Keluar Dari Program", 9*"-")
        print()
        break
    else:
        print()
        print(8*"-", "Salah Masukkan Angka", 8*"-")
        print("-Silahkan Masukkan Angka Dengan Benar-")