# Sistem Penilaian Akhir Mahasiswa
# Tambahkan fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(uts, uas):
    nilai_akhir = (uts + uas) / 2
    return nilai_akhir

# Tambahkan fungsi untuk menghitung nilai akhir semua mahasiswa
def hitung_nilai_akhir_semua(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        uts, uas = nilai
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        # Data mahasiswa (nama sebagai key dan nilai UTS serta UAS sebagai value dalam bentuk dictionary)
        "Asep": (100, 20),
        "Jamal": (50, 90),
        "Budi": (90, 95),
    }

    data_nilai_akhir = hitung_nilai_akhir_semua(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()