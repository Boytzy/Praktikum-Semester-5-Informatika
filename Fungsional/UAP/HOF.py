def sisagold(a, b, fungsi_kurang):
    return fungsi_kurang(a, b)

# Fungsi kurang yang akan digunakan sebagai parameter
def kurang(x, y):
    return x - y

# Contoh penggunaan high-order function
hasil_sisagold = sisagold(10, 3, kurang)
print("Hasil sisagold menggunakan fungsi kurang:", hasil_sisagold)
