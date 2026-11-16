jumlah = int(input("Jumlah mahasiswa: "))

data = []
lulus = 0
tidak_lulus = 0

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama  : ")
    nilai = float(input("Nilai : "))
   
    if nilai >= 85:
        grade, ket = "A", "Sangat Baik"
    elif nilai >= 75:
        grade, ket = "B", "Baik"
    elif nilai >= 60:
        grade, ket = "C", "Cukup"
    else:
        grade, ket = "D", "Tidak Lulus"

   
    if grade == "D":
        tidak_lulus += 1
    else:
        lulus += 1

        data.append((nama, nilai, grade, ket))

print("\n==============================================")
print("       DAFTAR HASIL PENILAIAN MAHASISWA")
print("==============================================")
print(f"{'No':<4}{'Nama':<15}{'Nilai':<10}{'Grade':<8}{'Keterangan'}")
print("----------------------------------------------")

for i, (nama, nilai, grade, ket) in enumerate(data, start=1):
    print(f"{i:<4}{nama:<15}{nilai:<10.2f}{grade:<8}{ket}")

print("----------------------------------------------")
print("\n============= HASIL SELURUH =============")
print("Jumlah mahasiswa :", jumlah)
print("Jumlah lulus     :", lulus)
print("Jumlah tidak lulus:", tidak_lulus)
print("========================================")