expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# Fungsi pure-function untuk menambahkan pengeluaran baru ke dalam expenses
add_expense = lambda expenses, tanggal, deskripsi, jumlah: expenses + [{'tanggal': tanggal, 'deskripsi': deskripsi, 'jumlah': jumlah}]

# Fungsi pure-function untuk menghitung total pengeluaran harian
calculate_total_expenses = lambda expenses, date: sum(expense['jumlah'] for expense in expenses if expense['tanggal'] == date)

# Fungsi lambda expression untuk menghitung total pengeluaran harian
calculate_total_expenses_interactively = lambda expenses: calculate_total_expenses(expenses, input("Masukkan tanggal (YYYY-MM-DD): "))

# Fungsi list comprehension untuk menyaring pengeluaran berdasarkan tanggal tertentu
get_expenses_by_date = lambda date: [expense for expense in expenses if expense['tanggal'] == date]

# Fungsi generator untuk menghasilkan laporan pengeluaran harian dalam bentuk string
generate_expenses_report = lambda: ("\n".join(f"{expense['tanggal']}: {expense['deskripsi']} - {expense['jumlah']}" for expense in expenses))

# TODO: Mengubah fungsi 'get_user_input' menjadi lambda
get_user_input = lambda command: int(input(command))

def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    new_expenses = add_expense(expenses, date, description, amount)
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses

def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")

def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report()
    print(expenses_report)

def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")

def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            total_expenses = calculate_total_expenses(expenses, date)
            print(f"\nTotal Pengeluaran Harian ({date}): Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")

if __name__ == "__main__":
    main()
