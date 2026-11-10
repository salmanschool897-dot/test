#Tugas 1
def celcius_ke_fahrenheit(celcius):
    hasil=(celcius*(9/5))+32
    print(hasil) 

celcius_ke_fahrenheit(0)   
celcius_ke_fahrenheit(100)

#tugas 2
def is_genap(bilangan):
    print(bilangan % 2 == 0)

is_genap(4)  # Output: True
is_genap(7)  # Output: False

#Tugas 3
def nilai(skor):
    if skor >= 80:
        print ("lulus")
    elif skor <= 60:
        print("gagal")
    else :
        print("Cukup")         

#nilai(88)
#nilai(70)
#nilai(50)         

#Tugas 4
def bilangan(angka):
    for i in range (1, angka + 1):
        if i % 2 != 0:
            print(i, end="")
bilangan(20)