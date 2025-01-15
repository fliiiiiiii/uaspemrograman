from data.sepatu1 import Data_Pendaftaran

class view_pendaftaran:
    def get_input():
        print("Buat pesanan anda")
        nama = input("Nama: ")
        brand = input("Brand sepatu: ")
        ukuran = input("Ukuran sepatu: ")
        return nama, brand, ukuran

    def table_view(data_table):
        print("=" * 60)
        print("| NO |           NAMA           |     BRAND     |  UKURAN  |")
        print("=" * 60)

        for i, data in enumerate(data_table, start=1):
            print(f"| {i:<2} | {data.nama:<24} | {data.brand:<13} | {data.ukuran:<8} |")
        print("=" * 60)

    def display_message(message):
        print(message)
