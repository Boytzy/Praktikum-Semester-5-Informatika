def hitung_pangkat(n):
    def pangkat(x):
        return x ** n
    return pangkat

# Contoh penggunaan
pangkat_dua = hitung_pangkat(2)
pangkat_tiga = hitung_pangkat(3)

print("Pangkat dua dari 4:", pangkat_dua(4))  # Output: 16
print("Pangkat tiga dari 4:", pangkat_tiga(4))  # Output: 64
