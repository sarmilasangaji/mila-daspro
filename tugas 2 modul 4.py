def hitung_nilai_kehadiran(jumlah_kehadiran):
    return jumlah_kehadiran * 16

def hitung_nilai_tugas(nilai_tugas):
    return sum(nilai_tugas)

def hitung_nilai_akhir(nilai_kehadiran, nilai_tugas, nilai_uts, nilai_uas):
    total_nilai_kehadiran = hitung_nilai_kehadiran(nilai_kehadiran)
    total_nilai_tugas = hitung_nilai_tugas(nilai_tugas)
    nilai_akhir = total_nilai_kehadiran + total_nilai_tugas + nilai_uts + nilai_uas
    return nilai_akhir

def tentukan_hasil(nilai_akhir):
    if nilai_akhir >= 90:
        return "A"
    elif nilai_akhir >= 80:
        return "B"
    elif nilai_akhir >= 70:
        return "C"
    elif nilai_akhir >= 60:
        return "D"
    elif nilai_akhir <= 60:
        return "E"

# Input nilai
nilai_kehadiran = int(input("Masukkan jumlah kehadiran mahasiswa: "))
nilai_tugas = [int(input(f"Masukkan nilai tugas ke-{i+1}: ")) for i in range(8)]
nilai_uts = int(input("Masukkan nilai UTS: "))
nilai_uas = int(input("Masukkan nilai UAS: "))

# Hitung nilai akhir
nilai_akhir = hitung_nilai_akhir(nilai_kehadiran, nilai_tugas, nilai_uts, nilai_uas)

# Tentukan hasil kelulusan
hasil = tentukan_hasil(nilai_akhir)

# Cetak hasil
print("Nilai akhir mahasiswa adalah:", nilai_akhir)
print("Hasil kelulusan mahasiswa:", hasil)
