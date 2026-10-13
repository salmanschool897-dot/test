#TUGAS NOMOR 1

kendaraan = ["Astrea", "Motor", 150, "Grey", 2]
tambahan = [400000, "Gigi"]
kendaraan.extend(tambahan)
kendaraan.insert(2, "MotoGP")
print(kendaraan)

#TUGAS NOMOR 2

print("=== Alat hitung luas bangun datar ====")
print("=== Alat hitung luas persegi ====")
print("=== Alat hitung luas lingkaran ====")
print("=== Alat hitung luas segitiga ====")

pilihan = int(input("Masukkan pilihan (1/2/3)"))
match pilihan:
    case 1: 
        s = int(input("Masukkan panjang sisi persegi: "))
        luas = s * s 
        print(f"Luas persegi adalah: {luas}")
    case 2:
        int(input("Masukkan panjang jari-jari lingkaran: "))
        pi = 3,14
        luas = pi * r**2
        print(f"luas lingkaran adalah: {luas}")
    case 3:
        a = int(input("Masukkan panjang alas segitiga: "))
        t = int(input("Masukkan panjang segitiga")) 
        luas = a * t / 2
        print(f"Luas segitiga adalah: {luas}")
         
#biodata.append("pelajar")
#biodata.remove("Depok")
#biodata.pop(0)
#biodata.insert(1, "0110126119")
#c = buah + biodata
#d = c + buah
#print(d)

#print(type(a))
#print(type(buah))
#print(type(biodata)))

#print("nama saya adalah", biodata[0])
#print("umur saya", biodata[1])
#print("saya tinggal di", biodata[2])
#print("berat badan saya", biodata[3])
#print("buah favorite saya adalah", buah[0])


#   MATCH 

cuaca = "Baadai"

#match cuaca:
 #   case "mendung":
  #      print("saya ke kampus ngebut")
   # case "hujan | badai":
    #@    print("saya ke kampus make jas hujan dan naik motor")
    #case "cerah":
    #    print("saya akan ke kampus seperti biasa")
    #case _:
     #   print("jalan aja dah")