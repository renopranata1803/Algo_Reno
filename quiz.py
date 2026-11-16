print("PROGRAM KELULUSAN UJIAN MATETMATIKA")
nama = input("Nama : ")

if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    target = int(
        input(f"Masukan Target Nilai Khusus Untuk {nama} : "))
print(f"masukan  Target nilai khusus untuk {nama} adalah: {target}\n")

percobaan = 0
berhasil_lulus = False

while percobaan < 3:
    percobaan += 1
    nilai = int(input(f"Nilai {percobaan} : "))

if nilai >= target:
    berhasil_lulus = True
 

print ("\n--- Hasil ----")
if   berhasil_lulus:
    print (f"{nama} berhasil lulus setelah {percobaan} kali percobaan [span_8](start_span)(span_8)(end_span)!")
else:
    print(f"{nama} tidak lulus setelah 3 kali percobaan!")