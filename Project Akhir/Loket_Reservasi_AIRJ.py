import os
os.system('cls')

print()
print("Tugas Project Akhir")
print("Kelompok 6")
print("1. Alif Maulana Setyawan")
print("2. Rezky Nur Sya'ban")
print("3. Muhammad Irsyadul Asyrof Haryono")

# Tuple

data1 = "101", "Garuda", "Jakarta", "09.30", 1500000
data2 = "102", "Citilink", "Surabaya", "12.30", 975000
data3 = "103", "Lion Air", "Semarang", "15.30", 920000
data4 = "104", "Batik Air", "Yogyakarta", "16.00", 1000000

# List

data_pemesan = []

data_tiket = [["101", "Garuda", "Jakarta", "09.30", 1500000],
              ["102", "Citilink", "Surabaya", "12.30", 975000],
              ["103", "Lion Air", "Semarang", "15.30", 920000],
              ["104", "Batik Air", "Yogyakarta", "16.00", 1000000]]

def daftar():
    print(38*"=")
    print("------------Daftar Pesanan------------")
    print(38*"=")
    for a, b, c, d, e in data_tiket:
        print(38*"-")
        print("Kode        :", a, 
              "\nPesawat     :", b, 
              "\nTujuan      :", c, 
              "\nJam         :", d, 
              "\nHarga Tiket :","Rp.", e)

def tambah():

    daftar()
    print()
    while True:
        try:
            print(38*"=")
            kode = int(input("Masukkan Kode Pesawat = "))
            print(38*"=")
            break

        except ValueError:
            print()
            print("-----Input Salah (Masukkan Angka)-----")
            print()
        
    if kode == 101 :
        os.system('cls')
        print()
        print("Kode          :", data1[0],
              "\nPesawat       :", data1[1],
              "\nTujuan        :", data1[2],
              "\nJam Berangkat :", data1[3],
              "\nHarga         :","Rp.",data1[4])
        print()

        print(60*"=")

        nama = input("Masukkan Nama Lengkap Pemesan       = ")
        nohp = input("Masukkan Nomor Handphone yang Aktif = ")
        while True:
            try:
                jumlah = int(input("Masukkan Jumlah Pesanan             = "))
                break

            except ValueError:
                print()
                print("--------------Input Salah (Masukkan Angka)------------------")
                print()
        
        if jumlah <= 0:
            print()
            print("~~~~~~~~~~~~Tidak Dapat Memesan 0 atau Dibawahnya~~~~~~~~~~~")
        else :
            total = jumlah * data_tiket[0][4]
            data_pemesan.append([data1[1], data1[2], data1[3], nama, nohp, total])

            print(60*"=")

            os.system('cls')
            
            # Struk

            print()
            print("=====================Struk Pembayaran=======================")
            print("Pesawat           :", data1[1],
                "\nTujuan            :", data1[2],
                "\nJam Berangkat     :", data1[3])
            print("Nama              :", nama,
                "\nNomor Handphone   :", nohp)
            print("Total Pembayaran  :","Rp.",total)
            print("============================================================")


    elif kode == 102 :
        os.system('cls')
        print()
        print("Kode          :", data2[0],
              "\nPesawat       :", data2[1],
              "\nTujuan        :", data2[2],
              "\nJam Berangkat :", data2[3],
              "\nHarga         :","Rp.",data2[4])
        print()

        print(60*"=")

        nama = input("Masukkan Nama Lengkap Pemesan       = ")
        nohp = input("Masukkan Nomor Handphone yang Aktif = ")
        while True:
            try:
                jumlah = int(input("Masukkan Jumlah Pesanan             = "))
                break

            except ValueError:
                print()
                print("--------------Input Salah (Masukkan Angka)------------------")
                print()

        if jumlah <= 0:
            print()
            print("~~~~~~~~~~~~Tidak Dapat Memesan 0 atau Dibawahnya~~~~~~~~~~~")
        else:
            total = jumlah * data_tiket[1][4]
            data_pemesan.append([data2[1], data2[2], data2[3], nama, nohp, total])

            print(60*"=")

            os.system('cls')
            
            # Struk

            print()
            print("=====================Struk Pembayaran=======================")
            print("Pesawat           :", data2[1],
                "\nTujuan            :", data2[2],
                "\nJam Berangkat     :", data2[3])
            print("Nama              :", nama,
                "\nNomor Handphone   :", nohp)
            print("Total Pembayaran  :","Rp.",total)
            print("============================================================")
        
    elif kode == 103 :
        os.system('cls')
        print()
        print("Kode          :", data3[0],
              "\nPesawat       :", data3[1],
              "\nTujuan        :", data3[2],
              "\nJam Berangkat :", data3[3],
              "\nHarga         :","Rp.",data3[4])
        print()

        print(60*"=")

        nama = input("Masukkan Nama Lengkap Pemesan       = ")
        nohp = input("Masukkan Nomor Handphone yang Aktif = ")
        while True:
            try:
                jumlah = int(input("Masukkan Jumlah Pesanan             = "))
                break

            except ValueError:
                print()
                print("--------------Input Salah (Masukkan Angka)------------------")
                print()

        if jumlah <= 0:
            print()
            print("~~~~~~~~~~~~Tidak Dapat Memesan 0 atau Dibawahnya~~~~~~~~~~~")
        else:
            total = jumlah * data_tiket[2][4]
            data_pemesan.append([data3[1], data3[2], data3[3], nama, nohp, total])
                
            print(60*"=")

            os.system('cls')
            
            # Struk

            print()
            print("=====================Struk Pembayaran=======================")
            print("Pesawat           :", data3[1],
                "\nTujuan            :", data3[2],
                "\nJam Berangkat     :", data3[3])
            print("Nama              :", nama,
                "\nNomor Handphone   :", nohp)
            print("Total Pembayaran  :","Rp.",total)
            print("============================================================")

    elif kode == 104 :
        os.system('cls')
        print()
        print("Kode          :", data4[0],
              "\nPesawat       :", data4[1],
              "\nTujuan        :", data4[2],
              "\nJam Berangkat :", data4[3],
                "\nHarga         :","Rp.",data4[4])
        print()
            
        print(60*"=")

        nama = input("Masukkan Nama Lengkap Pemesan       = ")
        nohp = input("Masukkan Nomor Handphone yang Aktif = ")
        while True:
            try:
                jumlah = int(input("Masukkan Jumlah Pesanan             = "))
                break

            except ValueError:
                print()
                print("--------------Input Salah (Masukkan Angka)------------------")
                print()

        if jumlah <= 0:
            print()
            print("~~~~~~~~~~~~Tidak Dapat Memesan 0 atau Dibawahnya~~~~~~~~~~~")
        else:
            total = jumlah * data_tiket[3][4]
            data_pemesan.append([data4[1], data4[2], data4[3], nama, nohp, total])

            print(60*"=")

            os.system('cls')
            
            # Struk

            print()
            print("=====================Struk Pembayaran=======================")
            print("Pesawat           :", data4[1],
                "\nTujuan            :", data4[2],
                "\nJam Berangkat     :", data4[3])
            print("Nama              :", nama,
                "\nNomor Handphone   :", nohp)
            print("Total Pembayaran  :","Rp.",total)
            print("============================================================")
            
    else:
        os.system('cls')
        print()
        print("================================================")
        print("------------Kode Pesawat Tidak Ada--------------")
        print("================================================")
        print()
        print("---Coba Lagi (Dan Masukkan Kode Dengan Benar)---")
        print()

def menu():
    print("------------Reservasi AIRJ------------")
    print(38*"=")
    print()
    print("1. Daftar Tiket")
    print("2. Daftar Pesanan")
    print("3. Ubah Data Pesanan")
    print("4. Hapus Pesanan")
    print("5. Keluar Dari Program")

def daftar_pesanan():
    if len(data_pemesan) <= 0:
        print()
        print(51*"=")
        print("-----------------Tidak Ada Data--------------------")
        print(51*"=")
    else :
        print()
        print(60*"=")
        print("----------------------Daftar Pesanan------------------------")
        print(60*"=")
        no = 0
        for i, j, k, l, m, n in data_pemesan:
            no += 1
            print(60*"=")
            print("Nomor Antrian   :", no,
                "\nPesawat         :", i,
                "\nTujuan          :", j,
                "\nJam Berangkat   :", k,
                "\nNama            :", l,
                "\nNomor Handphone :", m,
                "\nHarga           :","Rp.",n)
            print(60*"=")

def ubah():
    print()
    if len(data_pemesan) <= 0:
        print(52*"=")
        print("------------------Tidak Ada Data--------------------")
        print(52*"=")
    else:
        print(38*"=")
        print("------------Daftar Pesanan------------")
        print(38*"=")
        no = 0
        for i, j, k, l, m, n in data_pemesan:
            no += 1
            print(38*"-")
            print("Nomor Antrian   :", no,
                "\nPesawat         :", i,
                "\nTujuan          :", j,
                "\nJam Berangkat   :", k,
                "\nNama            :", l,
                "\nNomor Handphone :", m,
                "\nHarga           :","Rp.",n)
            print(38*"-")
            print()

        print(90*"=")

        nama = input("Masukkan Nama Lengkap Pemesan (Baru/Tetap)                      = ")
        nohp = input("Masukkan Nomor Handphone yang Aktif (Baru/Tetap)                = ")
        while True:
            try:
                pilih = int(input("Masukkan Nomor Antrian Yang Ingin Diubah                        = "))
                pilih -= 1
                break
            except ValueError:
                print()
                print("----------------Input Salah (Masukkan Angka)-------------------")
                print()

        print(90*"=")

        os.system('cls')
        print()
        print("=========================")
        print("-------Ubah Pesanan------")
        print("=========================")

        for a, b, c, d, e in data_tiket:
            print("-------------------------")
            print("kode        :", a, 
                "\nPesawat     :", b, 
                "\nTujuan      :", c, 
                "\nJam         :", d, 
                "\nHarga Tiket :","Rp.",e)

            print()

        while True:
            try:
                print("==============================")
                kode = int(input("Masukkan Kode Pesawat = "))
                print("==============================")
                break

            except ValueError:
                print()
                print("-Input Salah (Masukkan Angka)-")
                print()
            False

        os.system('cls')
        print()
        if kode == 101 :
            print("Kode          :", data1[0],
                  "\nPesawat       :", data1[1],
                  "\nTujuan        :", data1[2],
                  "\nJam Berangkat :", data1[3],
                  "\nHarga         :","Rp.",data1[4])

            print()

            while True:
                try:
                    print("===========================================")
                    jumlah = int(input("Masukkan Jumlah Pesanan = "))
                    print("===========================================")
                    break

                except ValueError:
                    print()
                    print("--------Input Salah (Masukkan Angka)-------")
                    print()

            if jumlah <= 0:
                print()
                print("~~~Tidak Dapat Memesan 0 atau Dibawahnya~~~")
            else:
                total = jumlah * data_tiket[0][4]

                while True:
                    try:
                        data_pemesan[pilih] = [data1[1], data1[2], data1[3], nama , nohp, total]

                        print()

                        print("===========================================")
                        print("----------------Data Di Ubah---------------")
                        print("===========================================")
                        break
                    except IndexError:
                        print()
                        print("-----------Nomor Antrian Tidak Ada---------")
                        print("------------Silahkan Coba Kembali----------")
                    break
                
            
        elif kode == 102 :
            print("Kode          :", data2[0],
                  "\nPesawat       :", data2[1],
                  "\nTujuan        :", data2[2],
                  "\nJam Berangkat :", data2[3],
                  "\nHarga         :","Rp.",data2[4])

            print()

            while True :
                try:
                    print("===========================================")
                    jumlah = int(input("Masukkan Jumlah Pesanan = "))
                    print("===========================================")
                    break

                except ValueError:
                    print()
                    print("--------Input Salah (Masukkan Angka)-------")
                    print()

            if jumlah <= 0:
                print()
                print("~~~Tidak Dapat Memesan 0 atau Dibawahnya~~~")
            else:
                total = jumlah * data_tiket[1][4]

                while True:
                    try:
                        data_pemesan[pilih] = [data2[1], data2[2], data2[3], nama , nohp, total]

                        print()

                        print("===========================================")
                        print("----------------Data Di Ubah---------------")
                        print("===========================================")
                        break
                    except IndexError:
                        print()
                        print("-----------Nomor Antrian Tidak Ada---------")
                        print("------------Silahkan Coba Kembali----------")
                    break
            
        elif kode == 103 :
            print("Kode          :", data3[0],
                  "\nPesawat       :", data3[1],
                  "\nTujuan        :", data3[2],
                  "\nJam Berangkat :", data3[3],
                  "\nHarga         :","Rp.",data3[4])

            print()

            while True :
                try:
                    print("===========================================")
                    jumlah = int(input("Masukkan Jumlah Pesanan = "))
                    print("===========================================")
                    break

                except ValueError:
                    print()
                    print("--------Input Salah (Masukkan Angka)-------")
                    print()

            if jumlah <= 0:
                print()
                print("~~~Tidak Dapat Memesan 0 atau Dibawahnya~~~")
            else:
                total = jumlah * data_tiket[2][4]

                while True:
                    try:
                        data_pemesan[pilih] = [data3[1], data3[2], data3[3], nama , nohp, total]

                        print()

                        print("===========================================")
                        print("----------------Data Di Ubah---------------")
                        print("===========================================")
                        break
                    except IndexError:
                        print()
                        print("-----------Nomor Antrian Tidak Ada---------")
                        print("------------Silahkan Coba Kembali----------")
                    break
            
        elif kode == 104 :
            print("Kode          :", data4[0],
                  "\nPesawat       :", data4[1],
                  "\nTujuan        :", data4[2],
                  "\nJam Berangkat :", data4[3],
                  "\nHarga         :","Rp.",data4[4])

            print()

            while True:
                try:
                    print("===========================================")
                    jumlah = int(input("Masukkan Jumlah Pesanan = "))
                    print("===========================================")
                    break
            
                except ValueError:
                    print()
                    print("--------Input Salah (Masukkan Angka)-------")
                    print()

            if jumlah <= 0:
                print()
                print("~~~Tidak Dapat Memesan 0 atau Dibawahnya~~~")
            else:
                total = jumlah * data_tiket[3][4]

                while True:
                    try:
                        data_pemesan[pilih] = [data4[1], data4[2], data4[3], nama , nohp, total]

                        print()

                        print("===========================================")
                        print("----------------Data Di Ubah---------------")
                        print("===========================================")
                        break
                    except IndexError:
                        print()
                        print("-----------Nomor Antrian Tidak Ada---------")
                        print("------------Silahkan Coba Kembali----------")
                    break
            
        else:
            print("================================================")
            print("------------Kode Pesawat Tidak Ada--------------")
            print("================================================")
            print()
            print("-------------Silahkan Coba Kembali--------------")
            
def hapus():
    print()
    if len(data_pemesan) <= 0:
        print(52*"=")
        print("------------------Tidak Ada Data--------------------")
        print(52*"=")
    else:
        print(38*"=")
        print("------------Daftar Pesanan------------")
        print(38*"=")
        no = 0
        for i, j, k, l, m, n in data_pemesan:
            no += 1
            print(38*"-")
            print("Nomor Antrian   :", no,
                "\nPesawat         :", i,
                "\nTujuan          :", j,
                "\nJam Berangkat   :", k,
                "\nNama            :", l,
                "\nNomor Handphone :", m,
                "\nHarga           :","Rp.",n)
            print(38*"-")
            print()
        
        print("--------------------------------------------")
        print("Peringatan : Data yang dipilih akan terhapus")
        print("--------------------------------------------")
        print()

        while True:
            try:
                print (65*"=")
                indeks = (int(input("Masukkan Nomor Antrian Yang Ingin Dihapus                  = ")))
                indeks -= 1
                print (65*"=")
                break

            except ValueError:
                print()
                print("-------------------Input Salah (Masukkan Angka)------------------")
                print()

        while True :
            try:
                del data_pemesan[indeks]
                
                print()
                print (65*"=")
                print (25*"-", "Data Di Hapus", 25*"-")
                print (65*"=")
                break
            except IndexError:
                print()
                print("--------------------Nomor Antrian Tidak Ada----------------------")
                print("---------------------Silahkan Coba Kembali-----------------------")
            break

# Program Utama

while True :
    print()
    print (38*"=")
    print (11*"-", "Selamat Datang", 11*"-")
    print (38*"=")
    menu()
    print()
    print(38*"=")
    x = input('Masukkan Menu [1-5] : ')
    print(38*"=")

    if x == '1' :
        os.system('cls')
        print()
        daftar()
        hitung = 0
        while hitung < 3 :
            print()
            print(49*"=")
            pesan = input("Apakah Ingin Memesan Tiket ? [ya/tidak] : ")
            print(49*"=")

            if pesan == 'ya':
                os.system('cls')
                tambah()
            elif pesan == 'tidak':
                break
            else:
                print()
                print("-------Input Salah (Masukkan Dengan Benar)-------")
                hitung += 1
                if hitung == 3:
                    break

            
    elif x == '2' :
        os.system('cls')
        daftar_pesanan()

    elif x == '3' :
        os.system('cls')
        hitung = 0
        while hitung < 3 :
            print()
            print(52*"=")
            pesan = input("Apakah ingin Mengubah Pesanan ? [ya/tidak] : ")
            print(52*"=")

            if pesan == 'ya':
                os.system('cls')
                ubah()
            elif pesan == 'tidak':
                break
            else:
                print()
                print("---------Input Salah (Masukkan Dengan Benar)--------")
                hitung += 1
                if hitung == 3:
                    break

    elif x == '4' :
        os.system('cls')
        hitung = 0
        while hitung < 3 :
            print()
            print(52*"=")
            pesan = input("Apakah ingin Menghapus Pesanan ? [ya/tidak]: ")
            print(52*"=")

            if pesan == 'ya':
                os.system('cls')
                hapus()
            elif pesan == 'tidak':
                break
            else:
                print()
                print("---------Input Salah (Masukkan Dengan Benar)--------")
                hitung += 1
                if hitung == 3:
                    break 

    elif x == '5' :
        os.system('cls')
        print()
        print (38*"=")
        print (9*"-", "Keluar Dari Program", 8*"-")
        print (38*"=")
        print()
        print ("--------------------------------------")
        print ("-----------Terimakasih, See u---------")
        print ("--------------------------------------")
        break
    else:
        os.system('cls')
        print()
        print(14*"-", "Salah Masukkan Angka", 15*"-")
        print("--------Silahkan Masukkan Angka Dengan Benar-------")

    print()
    hitung = 0
    while hitung < 3 :
        print(51*"=")
        kembali = input("Apakah ingin kembali ke menu ? [ya/tidak] : ")
        print(51*"=")
        if kembali == 'ya':
            os.system('cls')
            break
        elif kembali == 'tidak':
            os.system('cls')
            print()
            print(51*"=")
            print(15*"-", "Keluar Dari Program", 15*"-")
            print(51*"=")
            exit()
        else:
            print()
            print("--------Input Salah (Masukkan Dengan Benar)--------")
            print()
            hitung += 1
            if hitung == 3:
                print(51*"=")
                print(15*"-", "Keluar Dari Program", 15*"-")
                print(51*"=")
                exit()