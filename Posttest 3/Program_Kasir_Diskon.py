list_pesanan = {}

def makanan () :
    makan = {
        "kentang" : 13000,
        "tahu crispy" : 13000,
        "roti bakar" : 15000,
        "hamburger" : 15000,
        "pisang cokelat" : 12000
    }
    for simbol, nilai in makan.items():
        print(simbol,'\t> Rp.', nilai)

    print()
    print (40*"=")
    print (15*"-", "Pesanan", 16*"-")
    print (40*"=")
    a = makan[input("Masukkan Nama Menu      = ")]
    b = int(input("Masukkan Jumlah Pesanan = "))
    c = input("Hari                    = ")
    print (40*"=")
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
            print (40*"=")

            bayar = input("Bayar Pakai E-Money ? [y/n] : ")
            if bayar == "y" :
                hasil = y * (5/100)
                pembayaran = (int(y - hasil))
                print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                print (40*"=")
                
                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, pembayaran]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, y]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, y]

        else :
            persentase = 10/100
            x = jumlah * persentase
            y = (int(jumlah - x))
            print ("Diskon Weekdays 10 %")
            print ("Total Belanja + Diskon   = ", 'Rp.', y)
            print (40*"=")

            bayar = input("Bayar Pakai E-Money ? [y/n] : ")
            if bayar == "y" :
                hasil = y * (5/100)
                pembayaran = (int(y - hasil))
                print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, pembayaran]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, pembayaran]

            else :
                print ("Total Bayar             = ", 'Rp.', y)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, y]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, y]


    elif c in ("sabtu", "minggu"):
        if b >= 2 :
            persentase = 5/100
            diskon = jumlah * persentase
            print ("Diskon Weekend 5 % + Diskon Beli 2")
            x = diskon + (diskon * (1 - persentase))
            y = (int(jumlah - x))
            print ("Total Belanja + Diskon   = ", 'Rp.', y)
            print (40*"=")

            bayar = input("Bayar Pakai E-Money ? [y/n] : ")
            if bayar == "y" :
                hasil = y * (5/100)
                pembayaran = (int(y - hasil))
                print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, pembayaran]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, y]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, y]

        else :
            persentase = 5/100
            x = jumlah * persentase
            y = (int(jumlah - x))
            print ("Diskon Weekend 5 %")
            print ("Total Belanja + Diskon   = ", 'Rp.', y)
            print (40*"=")

            bayar = input("Bayar Pakai E-Money ? [y/n] : ")
            if bayar == "y" :
                hasil = y * (5/100)
                pembayaran = (int(y - hasil))
                print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, pembayaran]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, y]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, y]

def minuman ():
    minum = {
        "kopi caramel" : 20000,
        "kopi latte" : 20000,
        "cappucino" : 15000,
        "moccacino" : 15000,
        "kopi robusta" : 12000
    }
    for simbol, nilai in minum.items():
        print(simbol,'\t> Rp.', nilai)

    print()
    print (40*"=")
    print (15*"-", "Pesanan", 16*"-")
    print (40*"=")
    a = minum[input("Masukkan Nama Menu      = ")]
    b = int(input("Masukkan Jumlah Pesanan = "))
    c = input("Hari                    = ")
    print (40*"=")
    jumlah = a * b

    if c in ("senin", "selasa", "rabu", "kamis", "Jumat") :
        if b >= 3 :
            persentase = 10/100
            diskon = jumlah * persentase
            print ("Diskon Weekdays 10 % + Diskon Beli 3")
            x = diskon + (diskon * (1 - persentase))
            y = (int(jumlah - x))
            print ("Total Belanja + Diskon   = ", 'Rp.', y)
            print (40*"=")

            bayar = input("Bayar Pakai E-Money ? [y/n] : ")
            if bayar == "y" :
                hasil = y * (5/100)
                pembayaran = (int(y - hasil))
                print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, pembayaran]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, y]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, y]

        else :
            persentase = 10/100
            x = jumlah * persentase
            y = (int(jumlah - x))
            print ("Diskon Weekdays 10 %")
            print ("Total Belanja + Diskon   = ", 'Rp.', y)
            print (40*"=")

            bayar = input("Bayar Pakai E-Money ? [y/n] : ")
            if bayar == "y" :
                hasil = y * (5/100)
                pembayaran = (int(y - hasil))
                print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, pembayaran]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, y]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, y]

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
            print (40*"=")

            bayar = input("Bayar Pakai E-Money ? [y/n] : ")
            if bayar == "y" :
                hasil = y * (5/100)
                pembayaran = (int(y - hasil))
                print ("Total Bayar + Diskon 5 % = ", 'Rp.', pembayaran)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, pembayaran]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, y]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, y]

        else :
            persentase = 5/100
            x = jumlah * persentase
            y = (int(jumlah - x))
            print ("Diskon Weekend 5 %")
            print ("Total Belanja + Diskon   = ", 'Rp.', y)
            print (40*"=")

            bayar = input("Bayar Pakai E-Money ? [y/n] : ")
            if bayar == "y" :
                hasil = y * (5/100)
                pembayaran = (int(y - hasil))
                print ("Total Bayar + Diskon 5 % = ", 'Rp.',pembayaran)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, pembayaran]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, pembayaran]

            else :
                print ("Total Bayar              = ", 'Rp.', y)
                print (40*"=")

                if len(list_pesanan) <= 0 :
                    list_pesanan[a] = [jumlah, y, y]
                else:
                    del list_pesanan[a]
                    list_pesanan[a] = [jumlah, y, y]

def lihat():
    print("Peringatan : \nMemasukkan menu baru akan menghapus daftar harga pesanan yang lama")
    print()
    print("==========================================================================")
    print("|---------------------------Daftar Harga Pesanan-------------------------|")
    if len(list_pesanan) <= 0:  
        print("==============================================================================")
        print("|-------------------------------Tidak Ada Pesanan----------------------------|")
        print("==============================================================================")
    else:
        no = 0
        for data in list_pesanan.items():
            no += 1
            print(74*"=")
            print("| {1:^15} | {2:^19} | {3:^17} | {4:^8} |".format("No", "Harga", "Total Harga", "Total Diskon", "Pembayaran")) 
            print(74*"=")
            print(f"| Rp.{data[0]:^12} | Rp.{data[1][0]:^16} | Rp.{data[1][1]:^14} | Rp.{data[1][2]:^7} |")
            print(74*"=")

def diskon () :
    print()
    print (36*"=")
    print (14*"-", "Diskon", 14*"-")
    print (36*"=")
    print ("[Diskon] \n1. Membeli 3 Minuman   > 10% \n2. Membeli 2 Makanan   > 5% \n3. Bayar Lewat E-money > 5% \n4. Weekend             > 5% \n5. Weekdays            > 10%")

def menu() :
    print (38*"=")
    print (11*"-", "Selamat Datang", 11*"-")
    print (38*"=")
    print (16*"-", "Menu", 16*"-")
    print (38*"=")
    print ("[1] Makanan \n[2] Minuman \n[3] Diskon \n[4] Lihat Hasil Harga Pesanan Terbaru \n[0] Exit")
    x = input('Masukkan Menu [1,2,3,4,0] : ')
    if x == "1" :
        list_pesanan.clear()
        print()
        print (11*"-", "Menu Makanan", 11*"-")
        makanan()
    elif x == "2" :
        list_pesanan.clear()
        print()
        print (11*"-", "Menu Minuman", 11*"-")
        minuman()
    elif x == "3" :
        print()
        diskon()
    elif x == "4" :
        print()
        lihat()
    elif x == "0":
        print("Apakah Anda Yakin ?")
    else:
        print("Salah Masukkan Angka \nSilahkan Masukkan Angka Dengan Benar")

#Program Utama 

while True :
    menu()
    x = (input("Kembali Ke Menu ? [y/n]: "))
    if x == "y":
        print(9*"-", "Silahkan Memilih", 9*"-")
        print()
    else:
        print("Terima Kasih Telah Berkunjung")
        break