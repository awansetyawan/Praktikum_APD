# Login Administrasi
 
admin = 'admin'
password_admin = 'admin'

# Login Pembeli

konsumen = 'kasir'
password_konsumen = 'kasir'

# List Menu

list_pesanan = {}
 
menu_makan =[["kentang"       , 13000],
            ["tahu krispy"    , 13000],
            ["roti bakar"     , 15000],
            ["hamburger"      , 15000],
            ["pisang cokelat" , 12000]]

menu_minum =[["kopi caramel"  , 20000],
            ["kopi latte"     , 20000],
            ["cappucino"      , 15000],
            ["moccacino"      , 15000],
            ["kopi robusta"   , 12000]]

# Fungsi-Fungsi Kasir

def makanan () :

    for data, nilai in menu_makan :
        print(data,'\t> Rp.', nilai)

    print()
    print (52*"=")
    print (21*"-", "Pesanan", 22*"-")
    print (52*"=")
    i = input("Masukkan Nama Menu                  = ")
    a = int(input("Masukkan Harga Makanan Yang dipilih = "))
    b = int(input("Masukkan Jumlah Pesanan             = "))
    c = input("Hari                                = ")
    print (52*"=")
    jumlah = a * b

    if c in ("senin", "selasa", "rabu", "kamis", "Jumat") :
        if b >= 2 :
            persentase1 = 10/100
            persentase2 = 5/100
            diskon1 = jumlah * persentase1
            diskon2 = jumlah * persentase2 
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
                    list_pesanan[i] = [a, jumlah, y, pembayaran]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (52*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[i] = [a, jumlah, y, y]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, y]

        else :
            persentase = 10/100
            x = jumlah * persentase
            y = (int(jumlah - x))
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
                    list_pesanan[i] = [a, jumlah, y, pembayaran]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, pembayaran]

            else :
                print ("Total Bayar             = ", 'Rp.', y)
                print (52*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[i] = [a, jumlah, y, y]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, y]


    elif c in ("sabtu", "minggu"):
        if b >= 2 :
            persentase = 5/100
            diskon = jumlah * persentase
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
                    list_pesanan[i] = [a, jumlah, y, pembayaran]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (52*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[i] = [a, jumlah, y, y]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, y]

        else :
            persentase = 5/100
            x = jumlah * persentase
            y = (int(jumlah - x))
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
                    list_pesanan[i] = [a, jumlah, y, pembayaran]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (52*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[i] = [a, jumlah, y, y]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, y]

def minuman ():

    for data, nilai in menu_minum:
        print(data,'\t> Rp.', nilai)

    print()
    print (52*"=")
    print (21*"-", "Pesanan", 22*"-")
    print (52*"=")
    i = input("Masukkan Nama Menu                  = ")
    a = int(input("Masukkan Harga Minuman Yang dipilih = "))
    b = int(input("Masukkan Jumlah Pesanan             = "))
    c = input("Hari                                = ")
    print (52*"=")
    jumlah = a * b

    if c in ("senin", "selasa", "rabu", "kamis", "Jumat") :
        if b >= 3 :
            persentase = 10/100
            diskon = jumlah * persentase
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
                    list_pesanan[i] = [a, jumlah, y, pembayaran]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (52*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[i] = [a, jumlah, y, y]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, y]

        else :
            persentase = 10/100
            x = jumlah * persentase
            y = (int(jumlah - x))
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
                    list_pesanan[i] = [a, jumlah, y, pembayaran]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (52*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[i] = [a, jumlah, y, y]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, y]

    elif c in ("sabtu", "minggu"):
        if b >= 3 :
            persentase1 = 5/100
            persentase2 = 10/100
            diskon1 = jumlah * persentase1
            diskon2 = jumlah * persentase2 
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
                    list_pesanan[i] = [a, jumlah, y, pembayaran]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (52*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[i] = [a, jumlah, y, y]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, y]

        else :
            persentase = 5/100
            x = jumlah * persentase
            y = (int(jumlah - x))
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
                    list_pesanan[i] = [a, jumlah, y, pembayaran]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (52*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[i] = [a, jumlah, y, y]
                else:
                    del list_pesanan[i]
                    list_pesanan[i] = [a, jumlah, y, y]

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
            print()
            print (11*"-", "Menu Makanan", 11*"-")
            print()
            makanan()
        elif x == "2" :
            list_pesanan.clear()
            print()
            print (11*"-", "Menu Minuman", 11*"-")
            print()
            minuman()
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

# Fungsi-Fungsi Menu

def tambah():
    print()
    print (38*"=")
    print (10*"-", "Tambah Data Menu", 10*"-")
    print (38*"=")
    print ("[1] Makanan \n[2] Minuman")
    x = input('Masukkan Menu [1 atau 2] : ')
    if x == '1':
        print()
        print (12*"-", "Pilih Posisi", 12*"-")
        print ("[1] Tengah \n[2] Belakang")
        x = input('Masukkan Menu [1 atau 2] : ')

        if x == '1':
            print()
            print (61*"=")
            print (18*"-", "Silahkan Tambahkan Data", 18*"-")
            print (61*"=")

            for data, nilai in menu_makan :
                print(data,'\t >>', nilai)
            print()
            urut = int(input("Masukkan Nomor Posisi (Dimulai dari angka 0) = "))
            nama = (input("Masukkan Nama Menu Baru = "))
            harga = int(input("Masukkan Harga          = "))
            menu_makan.insert(urut, [nama, harga])
            print (61*"=")
            print (22*"-", "Data Ditambahkan", 21*"-")
            print (61*"=")

        elif x == '2':
            print()
            print (61*"=")
            print (18*"-", "Silahkan Tambahkan Data", 18*"-")
            print (61*"=")

            for data, nilai in menu_makan :
                print(data,'\t >>', nilai)
            print()
            nama = (input("Masukkan Nama Menu Baru = "))
            harga = int(input("Masukkan Harga          = "))
            menu_makan.append([nama , harga])
            print (61*"=")
            print (22*"-", "Data Ditambahkan", 21*"-")
            print (61*"=")

        else:
            print()
            print(8*"-", "Salah Masukkan Angka", 8*"-")
            print("-Silahkan Masukkan Angka Dengan Benar-")

    elif x == '2':
        print()
        print (12*"-", "Pilih Posisi", 12*"-")
        print ("[1] Tengah \n[2] Belakang")
        x = input('Masukkan Menu [1 atau 2] : ')

        if x == '1':
            print()
            print (61*"=")
            print (18*"-", "Silahkan Tambahkan Data", 18*"-")
            print (61*"=")

            for data, nilai in menu_minum :
                print(data,'\t >>', nilai)
            print()
            urut = int(input("Masukkan Nomor Posisi (Dimulai dari angka 0) = "))
            nama = (input("Masukkan Nama Menu Baru = "))
            harga = int(input("Masukkan Harga          = "))
            menu_minum.insert(urut, [nama, harga])
            print (61*"=")
            print (22*"-", "Data Ditambahkan", 21*"-")
            print (61*"=")

        elif x == '2':
            print()
            print (61*"=")
            print (18*"-", "Silahkan Tambahkan Data", 18*"-")
            print (61*"=")

            for data, nilai in menu_minum :
                print(data,'\t >>', nilai)
            print()
            nama = (input("Masukkan Nama Menu Baru = "))
            harga = int(input("Masukkan Harga          = "))
            menu_minum.append([nama , harga])
            print (61*"=")
            print (22*"-", "Data Ditambahkan", 21*"-")
            print (61*"=")

        else:
            print()
            print(8*"-", "Salah Masukkan Angka", 8*"-")
            print("-Silahkan Masukkan Angka Dengan Benar-")

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
        print()
        print (12*"-", "Pilih Metode", 12*"-")
        print ("[1] Hapus List Yang Dipilih \n[2] Hapus List Terbawah")
        x = input('Masukkan Menu [1 atau 2] : ')

        if x == '1':
            print()
            print (65*"=")
            print (22*"-", "Silahkan Hapus Data", 22*"-")
            print (65*"=")

            for data, nilai in menu_makan :
                print(data,'\t >>', nilai)
            print()
            indeks = (int(input("Masukkan Nomor List Menu Yang Ingin Dihapus (Dimulai dari 0) = ")))
            del menu_makan[indeks]
            print (65*"=")
            print (25*"-", "Data Di Hapus", 25*"-")
            print (65*"=")
        
        elif x == '2':
            print()
            menu_makan.pop()
            print (38*"=")
            print (8*"-", "Data Terbaru Di Hapus", 7*"-")
            print (38*"=")

        else:
            print()
            print(8*"-", "Salah Masukkan Angka", 8*"-")
            print("-Silahkan Masukkan Angka Dengan Benar-")

    elif x == '2':
        print()
        print (12*"-", "Pilih Metode", 12*"-")
        print ("[1] Hapus List Yang Dipilih \n[2] Hapus List Terbaru")
        x = input('Masukkan Menu [1 atau 2] : ')

        if x == '1':
            print()
            print (65*"=")
            print (22*"-", "Silahkan Hapus Data", 22*"-")
            print (65*"=")

            for data, nilai in menu_minum :
                print(data,'\t >>', nilai)
            print()
            indeks = (int(input("Masukkan Nomor List Menu Yang Ingin Dihapus (Dimulai dari 0) = ")))
            del menu_minum[indeks]
            print (65*"=")
            print (25*"-", "Data Di Hapus", 25*"-")
            print (65*"=")

        elif x == '2':
            print()
            menu_minum.pop()
            print (38*"=")
            print (8*"-", "Data Terbaru Di Hapus", 7*"-")
            print (38*"=")

        else:
            print()
            print(8*"-", "Salah Masukkan Angka", 8*"-")
            print("-Silahkan Masukkan Angka Dengan Benar-")
    
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
        print (23*"-", "Silahkan Ubah Data", 22*"-")
        print (65*"=")

        for data, nilai in menu_makan :
            print(data,'\t >>', nilai)
        print()
        pilih = int(input("Masukkan Nomor Urut Yang Ingin Diubah (Dimulai dari angka 0) = "))
        nama = input("Masukkan Nama Baru  = ")
        harga = int(input("Masukkan Harga Baru = "))
        menu_makan[pilih] = [nama , harga]
        print (65*"=")
        print (26*"-", "Data Di Ubah", 25*"-")
        print (65*"=")

    elif x == '2':
        print()
        print (65*"=")
        print (23*"-", "Silahkan Ubah Data", 22*"-")
        print (65*"=")

        for data, nilai in menu_minum :
            print(data,'\t >>', nilai)
        print()
        pilih = int(input("Masukkan Nomor Urut Yang Ingin Diubah (Dimulai dari angka 0) = "))
        nama = input("Masukkan Nama Baru  = ")
        harga = int(input("Masukkan Harga Baru = "))
        menu_minum[pilih] = [nama , harga]
        print (65*"=")
        print (26*"-", "Data Di Ubah", 25*"-")
        print (65*"=")
    
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
        print()
        print (38*"=")
        print (12*"-", "Menu Makanan", 12*"-")
        print (38*"=")

        for data, nilai in menu_makan :
            print(data,'\t >>', nilai)
    
    elif x == '2':
        print()
        print (38*"=")
        print (12*"-", "Menu Minuman", 12*"-")
        print (38*"=")

        for data, nilai in menu_minum :
            print(data,'\t >>', nilai)
    
    else:
        print()
        print(8*"-", "Salah Masukkan Angka", 8*"-")
        print("-Silahkan Masukkan Angka Dengan Benar-")

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