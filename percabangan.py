#nilai = int(input("Masukkan Nilai:"))

# if nilai >=80 and nilai <=100:
#    print("III PINTER A")
# elif nilai >=70 and nilai <=80:
#    print("BERJUANG LAGI B")
# elif nilai >=50 and nilai <=70:
#    print("SADIS YA NILAINYA C")
# elif nilai >=30 and nilai <=50:
#    print("NGERI KALI D")
# elif nilai >=0 and nilai <=20:
#      print("ANOMALI E")
# else:
#      print("NGULANG DONG")

print("======LATIHAN======")

barang = input("Masukkan Nama Barang:")
harga = input("Masukkan Harga Barang:")

if barang == "kulkas":
    print(barang)
    print(harga(harga * 0.10))
elif barang == "tv" :
    print(barang)
    print(harga(harga * 0.05))
else:
    print(barang)
    print(harga)