Data_Mahasiswa = {}

def garis():
    print(125*"=")

def header():
    garis()
    print("| {0:^4} | {1:^19} | {2:^19} | {3:^25} | {4:^8} | {5:^6} | {6:^22} |".format("No", "Nama", "NIM", "Prodi", "Kelas", "Gender", "IMT"))
    garis()

def tambah():
    print("Tambah data")
    nama       = input("Nama          : ")
    nim        = input("NIM           : ")
    prodi      = input("Prodi         : ")
    kelas      = input("Kelas (A,B,C) : ")
    gender     = input("L/P           : ")
    berat      = int(input("Berat (Kg)    : "))
    tinggi     = int(input("Tinggi (Cm)   : "))
    imt        = float(berat / ((tinggi/100)*(tinggi/100)))
    Data_Mahasiswa[nama] = [nim, prodi, kelas, gender, imt]
    print(f"Berhasil Menambahkan Data '{nama}' Dengan NIM : {nim}!")

def lihat():
    print("Daftar Mahasiswa")
    if len(Data_Mahasiswa) <= 0:  
        kosong()
    else:
        no = 0
        header()
        for data in Data_Mahasiswa.items():
            no += 1 
            print(f"| {no:^4} | {data[0]:^19} | {data[1][0]:^19} | {data[1][1]:^25} | {data[1][2]:^8} | {data[1][3]:^6} | {data[1][4]:^22} |")               
        garis()

def kosong(): 
    header()          
    print("|{0:^123}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
    garis()

def hapus():
    print("Hapus Data Mahasiswa Berdasarkan Nama")
    if len(Data_Mahasiswa) <= 0:  
        kosong()
    else:
        nama = input("Masukan nama : ")
        if(nama in Data_Mahasiswa):
            del Data_Mahasiswa[nama]
            print(f"Data {nama} Berhasil Dihapus!")
        else:
            print(f"Data {nama} Tidak Ditemukan!")

loop = True

# Program
while loop:
    print()
    print(71*"-")
    print(20*"-", "Program Data Mahasiswa & IMT", 21*"-")
    print(71*"-")
    print("[1] Tambah Data \n[2] Lihat Data  \n[3] Hapus Data \n[0] Keluar")
    print(71*"-")
    menu = int(input("Pilih Menu : "))
    print(71*"-")
    print()

    if menu == 1:
        tambah()       
    elif menu == 2:
        lihat()
    elif menu == 3:
        hapus() 
    elif menu == 0:
        print("Program Selesai, See U Next Time")
        loop = False 
    else:
        print(f"Menu '{menu}' Tidak Ada! Silahkan Masukan [0-4]")