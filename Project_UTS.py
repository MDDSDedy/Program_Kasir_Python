import sys
total = []

print("----------------- Program Kasir Dedy Jaya -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli)

#Fungsi Menu
def menu():
    print("\n")
    print("""
          ============================================

          Selamat Datang di Toko Dedy Jaya
          Sedia Komponen Elektronik Original
        
          [1] Resistor
          [2] Sensor
          [3] Mikrokontroller
          [4] Lampu LED
          [5] Total Belanja
          [6] Exit

          ============================================
          """)
    pesan = str(input("Masukkan Pilihan ="))
    print("\n")

    if pesan == "1":
        resistor()
    elif pesan =="2":
        sensor()
    elif pesan =="3":
        mikro()
    elif pesan =="4":
        led()
    elif pesan =="5":
        totalan()
    elif pesan == "6":
        exit()
    else:
        print("Pilihan yang anda masukan salah!")
        menu()

#Fungsi Resistor
def resistor():
    print("""
          ============================================
          Pilih Berapa Ohm ?
          [1] 100   Ohm         Rp 100
          [2] 1000  Ohm         Rp 200
          [3] 10000 Ohm         Rp 500
          [4] Exit
          ============================================
          """)
    res = str(input("Pilih No List Berapa Ohm ="))
    if res == "1":
        jml_res100 = int(input("Jumlah Pesanan Resistor 100 Ohm ="))
        harga_res100 = 100*jml_res100
        total.append(harga_res100)
        pilihan_res100 = input("Apakah Anda Ingin Order Resistor Kembali y/t =")
        if pilihan_res100 == "y":
            resistor()
        elif pilihan_res100 == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            resistor()
    elif res =="2":
        jml_res1k = int(input("Jumlah Pesanan Resistor 1000 Ohm ="))
        harga_res1k = 200*jml_res1k
        total.append(harga_res1k)
        pilihan_res1k = input("Apakah Anda Ingin Order Resistor Kembali y/t =")
        if pilihan_res1k == "y":
            resistor()
        elif pilihan_res1k == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            resistor()
    elif res =="3":
        jml_res10k = int(input("Jumlah Pesanan Resistor 10000 Ohm ="))
        harga_res10k = 500*jml_res10k
        total.append(harga_res10k)
        pilihan_res10k = input("Apakah Anda Ingin Order Resistor Kembali y/t =")
        if pilihan_res10k == "y":
            resistor()
        elif pilihan_res10k == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            resistor()
    elif res =="4":
        menu()
    else:
        print("Pilihan yang anda masukan salah!")
        resistor()

#Fungsi Sensor
def sensor():
    print("""
          ============================================
          Pilih Sensor Apa ?
          [1] Sensor Arus       Rp 10.000
          [2] Sensor Tegangan   Rp 20.000
          [3] Sensor Suhu       Rp 25.000
          [4] Exit
          ============================================
          """)
    
    ses = str(input("Pilih No List Sensor Apa ="))
    if ses == "1":
        jml_sesa = int(input("Jumlah Pesanan Sensor Arus ="))
        harga_sesa = 10000*jml_sesa
        total.append(harga_sesa)
        pilihan_sesa = input("Apakah Anda Ingin Order Sensor Kembali y/t =")
        if pilihan_sesa == "y":
            sensor()
        elif pilihan_sesa == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            sensor()
    elif ses =="2":
        jml_sest = int(input("Jumlah Pesanan Sensor Tegangan ="))
        harga_sest = 20000*jml_sest
        total.append(harga_sest)
        pilihan_sest = input("Apakah Anda Ingin Order Sensor Kembali y/t =")
        if pilihan_sest == "y":
            sensor()
        elif pilihan_sest == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            sensor()
    elif ses =="3":
        jml_sess = int(input("Jumlah Pesanan Sensor Suhu ="))
        harga_sess = 25000*jml_sess
        total.append(harga_sess)
        pilihan_sess = input("Apakah Anda Ingin Order Sensor Kembali y/t =")
        if pilihan_sess == "y":
            sensor()
        elif pilihan_sess == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            sensor()
    elif ses =="4":
        menu()
    else:
        print("Pilihan yang anda masukan salah!")
        sensor()
    

#Fungsi Mikrokontroller
def mikro():
    print("""
          ===============================================
          Pilih Mikrokontroller Apa ?
          [1] Arduino           Rp  50.000
          [2] STM32F4           Rp 100.000
          [3] Raspberry         Rp 500.000
          [4] Exit
          ===============================================
          """)
    mkt = str(input("Pilih No List Mikrokontroller Apa ="))
    if mkt == "1":
        jml_mkta = int(input("Jumlah Pesanan Arduino ="))
        harga_mkta = 50000*jml_mkta
        total.append(harga_mkta)
        pilihan_mkta = input("Apakah Anda Ingin Order Mikrokontroller Kembali y/t =")
        if pilihan_mkta == "y":
            mikro()
        elif pilihan_mkta == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            mikro()
    elif mkt =="2":
        jml_mkts = int(input("Jumlah Pesanan Sensor Tegangan ="))
        harga_mkts = 100000*jml_mkts
        total.append(harga_mkts)
        pilihan_mkts = input("Apakah Anda Ingin Order Mikrokontroller Kembali y/t =")
        if pilihan_mkts == "y":
            mikro()
        elif pilihan_mkts == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            sensor()
    elif mkt =="3":
        jml_mktr = int(input("Jumlah Pesanan Sensor Suhu ="))
        harga_mktr = 500000*jml_mktr
        total.append(harga_mktr)
        pilihan_mktr = input("Apakah Anda Ingin Order Mikrokontroller Kembali y/t =")
        if pilihan_mktr == "y":
            mikro()
        elif pilihan_mktr == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            mikro()
    elif mkt =="4":
        menu()
    else:
        print("Pilihan yang anda masukan salah!")
        mikro()

#Fungsi LED
def led():
    print("""
          Pilih Lampu LED Warna Apa ?
          [1] Biru              Rp 500
          [2] Hijau             Rp 500
          [3] Merah             Rp 500
          [4] Exit
          """)
    
    ll = str(input("Pilih No List LED Warna Apa ="))
    if ll == "1":
        jml_lb = int(input("Jumlah Pesanan LED Biru ="))
        harga_lb = 500*jml_lb
        total.append(harga_lb)
        pilihan_lb = input("Apakah Anda Ingin Order LED Kembali y/t =")
        if pilihan_lb == "y":
            led()
        elif pilihan_lb == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            led()
    elif ll =="2":
        jml_lh = int(input("Jumlah Pesanan LED Hijau ="))
        harga_lh = 500*jml_lh
        total.append(harga_lh)
        pilihan_lh = input("Apakah Anda Ingin Order LED Kembali y/t =")
        if pilihan_lh == "y":
            led()
        elif pilihan_lh == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            led()
    elif ll =="3":
        jml_lm = int(input("Jumlah Pesanan LED Merah ="))
        harga_lm = 500*jml_lm
        total.append(harga_lm)
        pilihan_lm = input("Apakah Anda Ingin Order LED Kembali y/t =")
        if pilihan_lm == "y":
            led()
        elif pilihan_lm == "t":
            menu()
        else:
            print("Pilihan yang anda masukan salah!")
            led()
    elif ll =="4":
        menu()
    else:
        print("Pilihan yang anda masukan salah!")
        led()

# FungsiTotalan
def totalan():
    for harga in total:
       print("SubTotal         : ", sum(total))
       diskon = 0
       a = sum(total)
       if a > 500000:
           diskon = a * 8/100
       elif a > 300000:
           diskon = a * 5/100
       elif a > 200000:
           diskon = a * 2/100
       elif a > 100000:
           diskon = a * 1/100
       else:
            diskon = 0       
       print("CashBack         : ", diskon)
       totalakhir = a - diskon
       print("Total            : ", totalakhir)
       print("-------------------------------")
       bayar = int(input("Bayar            :  "))
       kembalian = bayar - totalakhir
       print("Kembalian        : ", kembalian)
       print("-------------------------------")
       print("          Terima Kasih         ")
       print("-------------------------------")
       exit()

menu()