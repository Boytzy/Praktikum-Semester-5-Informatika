def tambah_angka(angka, total=0):
    return total + angka

# Contoh penggunaan
total_sekarang = 0
angka1 = 5
angka2 = 10

total_sekarang = tambah_angka(angka1, total_sekarang)
print(f"Total setelah tambah {angka1}: {total_sekarang}")

total_sekarang = tambah_angka(angka2, total_sekarang)
print(f"Total setelah tambah {angka2}: {total_sekarang}")
