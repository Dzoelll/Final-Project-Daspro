import datetime
import os

def clear():
    os.system('cls')

def intro():
    print("|==========================================================|")
    print("|Kelompok 2                                                |")
    print("""|  Anggota:                                                |
|      - Dzulfaraz Farouk Fauzi (19240330)                 |
|      - Aditya Pramadi (19242556)                         |
|      - Tiara (19241436)                                  |
|      - Rohyani (19242164)                                |       
|      - Syaqina Fauzurra Destini (19241564)               |""")
    print("|                                                          |")
    print("|  Tema : Penjualan & Pembelian - Bidang Matematika        |")
    print("|__________________________________________________________|\n")

    while input("KLIK 0 UNTUK LANJUTKAN : ") != "0":
        continue
    clear()

def daftar_menu():
    print("|--------------  MENU RESTAURANT BAKAR GULING   --------------|")
    print("|            MAKANAN            |           MINUMAN           |")
    print("| 1. [SB] Sosis Bakar     [5K]  | 7.  [TM] Es Teh Manis [5K]  |")
    print("| 2. [OB] Otak-Otak Bakar [5K]  | 8.  [TT] Es Teh Tawar [3K]  |")
    print("| 3. [BB] Bakso Bakar     [7K]  | 9.  [JR] Es Jeruk     [7K]  |")
    print("| 4. [NB] Nasi Bakar      [10K] | 10. [KP] Es Kopi      [7K]  |")
    print("| 5. [AB] Ayam Bakar      [25K] | 11. [BT] Es Batu      [2K]  |")
    print("| 6. [IB] Ikan Bakar      [25K] | 12. [AM] Air Mineral  [4K]  |\n")

menu = {
    "SB": 5000, "OB": 5000, "BB": 7000, "NB": 10000, "AB": 25000, "IB": 25000,
    "TM": 5000, "TT": 3000, "JR": 7000, "KP": 7000, "BT": 2000, "AM": 4000,
}

def pesan(item_type, valid_items):
    pesanan = []
    while True:
        item = input(f"Pilih Kode {item_type} : ")
        if item in valid_items:
            jumlah = int(input("> Masukkan Jumlah : "))
            pesanan.append((item, jumlah))
            if input(f"\nApakah Ada Tambahan {item_type}? (y/n) : ").lower() == "n":
                break
        else:
            print("\n| Menu Tidak Ditemukan, Masukan Kode Menu Yang Valid! |\n")
    return pesanan

def hitung_total(pesanan_makanan, pesanan_minuman):
    total = 0
    for item, jumlah in pesanan_makanan + pesanan_minuman:
        total += menu.get(item, 0) * jumlah
    return total

# Memulai pemesanan
intro()
daftar_menu()
pesanan_makanan = pesan("Makanan", ["SB", "OB", "BB", "NB", "AB", "IB"])
clear()
daftar_menu()
pesanan_minuman = pesan("Minuman", ["TM", "TT", "JR", "KP", "BT", "AM"])
clear()
nama_pemesan = input("\nMasukkan Nama Pemesan: ")
total_pembelian = hitung_total(pesanan_makanan, pesanan_minuman)
#jumlah_uang = int(input("Masukan Jumlah Uang: "))
clear()
#kembalian = jumlah_uang - total_pembelian
jumlah_uang = int(input("Masukan Jumlah Uang Pembayaran: "))
if jumlah_uang >= hitung_total( pesanan_makanan, pesanan_minuman):
    clear()
    print("\nPembayaaran Anda Berhasil\n")
else:
    while jumlah_uang < hitung_total(pesanan_makanan, pesanan_minuman):
        print("\nPembayaran Gagal! Masukan Nominal Yang Sesuai\n")
        jumlah_uang = int(input("Masukan Jumlah Uang Pembayaran: "))
    else :
        clear()
        print("\nPembayaran Anda Berhasil!\n")
kembalian = jumlah_uang - total_pembelian

# Menampilkan hasil
#print("\nPesanan Anda :")
#for item, jumlah in pesanan_makanan + pesanan_minuman:
 #   print(f"- {jumlah} {item}")
#print("\nNama Pemesan :", nama_pemesan)
#print("Total Pembelian :", total_pembelian)
#print("\nJumlah Uang Yang Diberikan : ", jumlah_uang)
#print("Uang Kembalian : ", kembalian)

# Menampilkan hasil
now = datetime.datetime.now()
print("\n|----------------------------------------------|")
print("|            RESTAURANT BAKAR GULING           |")
print(f"|          {now}          |")
print("|----------------------------------------------|")
print("|                                              |\n| PESANAN ANDA :                               |\n|                                              |")

# Membuat dictionary untuk mapping kode menu ke nama menu
menu_nama = {
    "SB": "Sosis Bakar", "OB": "Otak-Otak Bakar", "BB": "Bakso Bakar", "NB": "Nasi Bakar", "AB": "Ayam Bakar", "IB": "Ikan Bakar",
    "TM": "Es Teh Manis", "TT": "Es Teh Tawar", "JR": "Es Jeruk", "KP": "Es Kopi", "BT": "Es Batu", "AM": "Air Mineral",
}

# Menampilkan pesanan dengan nama menu dan subtotal
for item, jumlah in pesanan_makanan + pesanan_minuman:
    harga = menu.get(item, 0)
    subtotal = harga * jumlah
    print(f"|   - {jumlah} {menu_nama[item]}  (Rp {harga}) = Rp {subtotal}      |")

#
print("|                                              |\n|----------------------------------------------|")
print(f"|                                              |\n|    Nama Pemesan         : {nama_pemesan}               |")
print(f"|    Total Pembelian      : Rp {total_pembelian}           |")
print(f"|    Uang Yang Diberikan  : Rp {jumlah_uang}           |")
print(f"|    Kembalian            : Rp {kembalian}           |")
print("|                                              |\n|----------------------------------------------|")
print("|______________________________________________|")