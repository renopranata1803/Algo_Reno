jumlah = int(input("jumlah mahasiswa : "))
if jumlah <5 or jumlah >10:
    print("jumlah harus antara 5 sampai 10")
    jumlah=int(input("jumlah mahasiswa(5-10):"))
total = 0
for i in range(1,jumlah +1):
       nilai= int(input("masukkan nilai mahasiswa(i):"))
       total += nilai
       rata_rata = total / jumlah
       print("nilai rata-rata:", rata_rata)
       print("=====Hasil=====")
else:
      print("jumlah mahasiswa yang diinputkan harus 5 sampai 10")