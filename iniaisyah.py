import time

data1=input("masukan sebuah kalimat : ")
data2=input("karakter yang ingin di hitung jumlah nya: ")

print("Jumlah karakter{0}alam kalimat tersebut adalah {1}".format(data2 ,data1.count(data2)))

time.sleep(50)