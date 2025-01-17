import re
from data.sepatu1 import Data_Pendaftaran
from view.sepatu import view_pendaftaran


class process_pendaftaran:
    def validate_nama(nama):
        if not nama.isalpha():
            raise ValueError("nama hanya boleh berisi huruf.")
        
    def validate_brand(brand):
        if not brand.isalpha():
            raise ValueError("nama brand hanya boleh berisi huruf.")

    def validate_ukuran(ukuran):
        if not ukuran.isdigit():
            raise ValueError("ukuran hanya boleh berisi angka.")

   

    def validate_data(data):
        process_pendaftaran.validate_nama(data.nama)
        process_pendaftaran.validate_brand(data.brand)
        process_pendaftaran.validate_ukuran(data.ukuran)
