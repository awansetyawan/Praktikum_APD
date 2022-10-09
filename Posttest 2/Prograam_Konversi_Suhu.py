def menu():
    print ("==========Menu===========")
    print ("[1] Fahrenheit Ke Celcius")
    print ("[2] Kelvin Ke Celcius")
    print ("[3] Reamur Ke Celcius")
    print ("[4] Exit")

def suhu_1():
    f = int(input("Masukkan Suhu Dalam Fahrenheit (°F) : "))
    hasil_1 = float((f - 32) / 1.8)
    print (("Suhu Celcius nya = "), hasil_1, "°C")

def suhu_2():
    k = int(input("Masukkan Suhu Dalam Kelvin (°K): "))
    hasil_2 = float((k - 273.15))
    print (("Suhu Celcius nya = "), hasil_2, "°C")

def suhu_3():
    r = int(input("Masukkan Suhu Dalam Reamur (°R): "))
    hasil_3 = float((r / 0.8))
    print (("Suhu Celcius nya = "), hasil_3, "°C")

# Program Utama

print ("------------------Konversi Suhu---------------------")

print ()

menu()
pilih = int(input("Masukkan Menu : "))

while pilih != 4:
    if pilih == 1:
        suhu_1()
    elif pilih == 2:
        suhu_2()
    elif pilih == 3:
        suhu_3()
    else: 
        print("Salah Input")

    print()
    print ("Ingin Konversi lagi ? (y/n) : ")
    back = input("Pilih : ")
    if back == ("y") :
        print()
        menu()
        pilih = int(input("Masukkan Menu : "))
    else :
        print ("Bye")
        exit()

print("Terimakasih Telah Menggunakan Program Ini")
