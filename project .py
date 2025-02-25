import csv
import os

# Variabel untuk menyimpan file
namafile = r'C:\Users\Lenovo V330\Documents\python\karyawan.csv'

# Membuat file csv
def init_csv():
    if not os.path.exists(namafile):
        with open(namafile, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'Nama', 'Jabatan', 'Gaji'])

# Menambahkan karyawan
def tambah_karyawan(id, Nama, jabatan, gaji):
    with open(namafile, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, Nama, jabatan, gaji])
    print('Karyawan berhasil ditambahkan.')

# Menghapus karyawan
def hapus_karyawan(id):
    rows = []
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    found = False
    with open(namafile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])  
        
        for row in rows[1:]:
            if row[0] != id:
                writer.writerow(row)
            else:
                found = True
    
    if found:
        print(f'Karyawan dengan ID {id} berhasil dihapus.')
    else:
        print(f'Karyawan dengan ID {id} tidak ditemukan.')

# Memperbarui data karyawan
def update_karyawan(id, Nama=None, jabatan=None, gaji=None):
    rows = []
    found = False
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    with open(namafile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])  
        for row in rows[1:]:
            if row[0] == id:
                if Nama:
                    row[1] = Nama
                if jabatan:
                    row[2] = jabatan
                if gaji:
                    row[3] = gaji
                found = True
            writer.writerow(row)
    
    if found:
        print(f'Karyawan dengan ID {id} berhasil diperbarui.')
    else:
        print(f'Karyawan dengan ID {id} tidak ditemukan.')

# Menampilkan daftar karyawan
def tampilkan_karyawan():
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Mencari karyawan berdasarkan ID
def cari_karyawan(id):
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:
                print(f'Karyawan ditemukan: {row}')
                return
    print(f'Karyawan dengan ID {id} tidak ditemukan.')

# Menu utama
def menu():
    init_csv()
    while True:
        print("\n=== Sistem Manajemen Karyawan ===")
        print("1. Tambah Karyawan")
        print("2. Hapus Karyawan")
        print("3. Perbarui Karyawan")
        print("4. Tampilkan Semua Karyawan")
        print("5. Cari Karyawan")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            id = input("Masukkan ID: ")
            nama = input("Masukkan Nama: ")
            jabatan = input("Masukkan Jabatan: ")
            gaji = input("Masukkan Gaji: ")
            tambah_karyawan(id, nama, jabatan, gaji)
        elif pilihan == '2':
            id = input("Masukkan ID Karyawan yang akan dihapus: ")
            hapus_karyawan(id)
        elif pilihan == '3':
            id = input("Masukkan ID Karyawan yang akan diperbarui: ")
            nama = input("Masukkan Nama baru (kosongkan jika tidak ingin mengubah): ")
            jabatan = input("Masukkan Jabatan baru (kosongkan jika tidak ingin mengubah): ")
            gaji = input("Masukkan Gaji baru (kosongkan jika tidak ingin mengubah): ")
            update_karyawan(id, nama if nama else None, jabatan if jabatan else None, gaji if gaji else None)
        elif pilihan == '4':
            tampilkan_karyawan()
        elif pilihan == '5':
            id = input("Masukkan ID Karyawan yang dicari: ")
            cari_karyawan(id)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Memulai program
if __name__ == '__main__':
    menu()
