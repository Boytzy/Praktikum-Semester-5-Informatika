import os

# Inisialisasi database buku yang tersedia
books_available = {
    "11": "Belajar Pemrograman Fungsional",
    "22": "Belajar Pemrograman Web",
    "33": "Belajar Pemrograman Mobile",
}

# Inisialisasi database peminjaman buku
book_borrowed = {}

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menambahkan buku baru oleh admin
def add_book(book_id, book_title):
    books_available[book_id] = book_title
    print(f"Buku '{book_title}' dengan (ID: {book_id}) telah ditambahkan.")

# Fungsi untuk melakukan peminjaman buku oleh user
def borrow_book(book_id):
    global book_borrowed
    if book_id in books_available:
        if book_id not in book_borrowed:
            book_title = books_available[book_id]
            book_borrowed[book_id] = book_title
            print(f"Anda telah meminjam buku '{book_title}' (ID: {book_id}).")
        else:
            print("Buku ini sudah dipinjam oleh pengguna lain.")
    else:
        print("Buku dengan ID ini tidak tersedia.")

# Fungsi untuk mengembalikan buku oleh user
def return_book(book_id):
    global book_borrowed
    if book_id in book_borrowed:
        book_title = book_borrowed.pop(book_id)
        print(f"Anda telah mengembalikan buku '{book_title}' (ID: {book_id}).")
    else:
        print("Anda tidak memiliki buku ini untuk dikembalikan.")

# Fungsi untuk menampilkan buku yang tersedia
def show_available_books():
    print("\nBuku Tersedia:")
    for book_id, book_title in books_available.items():
        print(f"ID: {book_id} - Judul: {book_title}")


#Menu utama
def main():
    while True:
        clear_screen()
        print("\nSelamat datang di sistem manajemen perpustakaan!")
        print("Pilih jenis akun:")
        print("1. Admin")
        print("2. User")
        print("3. Keluar")
        choice = input("Masukkan pilihan Anda: ")

        if choice == "1":
            clear_screen()
            print("Selamat datang, admin!")
            while True:
                print("\nPilih aksi:")
                print("1. Tambahkan Buku")
                print("2. Keluar sebagai admin")
                sub_choice = input("Masukkan pilihan Anda: ")

                if sub_choice == "1":
                    book_id = input("Masukkan ID buku baru: ")
                    book_title = input("Masukkan judul buku baru: ")
                    add_book(book_id, book_title)
                elif sub_choice == "2":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif choice == "2":
            clear_screen()
            print("Selamat datang, user!")
            while True:
                print("\nPilih aksi:")
                print("1. Pinjam Buku")
                print("2. Kembalikan Buku")
                print("3. Tampilkan Buku Tersedia")
                print("4. Keluar sebagai user")
                sub_choice = input("Masukkan pilihan Anda: ")

                if sub_choice == "1":
                    book_id = input("Masukkan ID buku yang ingin Anda pinjam: ")
                    borrow_book(book_id)
                elif sub_choice == "2":
                    book_id = input("Masukkan ID buku yang ingin Anda kembalikan: ")
                    return_book(book_id)
                elif sub_choice == "3":
                    clear_screen()
                    show_available_books()  # Memanggil clear_screen() di sini akan membuat layar kosong.
                elif sub_choice == "4":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif choice == "3":
            break

        else:
            print("Pilihan tidak valid.")
if __name__ == "__main__":
    main()
