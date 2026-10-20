Nilai_tugas = int(input("masukkan nilai tugas:"))
Uts = int(input("masukkan nilai uts:"))
Uas = int(input("masukkan nilai uas:"))
kehadiran_Mahasiswa =int(input("masukkan nilai kehadiran:"))

nilai_akhir = (20 / 100 * Nilai_tugas) + (30 / 100 * Uts) + (50 / 100 * Uas)

print("======Hasil======")
print("Nilai_akhir =", nilai_akhir)
print(kehadiran_Mahasiswa, "%")

if nilai_akhir >= 80 and kehadiran_Mahasiswa >= 90:

    if nilai_akhir >= 80 and kehadiran_Mahasiswa >= 90 and nilai_akhir % 2 == 0:
        print("Status      : LULUS DENGAN PREDIKAT")
    elif nilai_akhir >= 70 and kehadiran_Mahasiswa >= 90:
        print("Status      : LULUS")
else:
    print("Status      :BELUM LULUS")