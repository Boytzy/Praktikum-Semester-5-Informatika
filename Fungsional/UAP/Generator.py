# Fungsi generator untuk menghasilkan angka ganjil antara 0 sampai 50
def generate_angka_ganjil():
    for angka in range(51):
        if angka % 2 != 0:
            yield angka

# Membuat objek generator dan langsung mengiterasinya
for angka in generate_angka_ganjil():
    print(angka)
