class Diskon:
    def __init__(self):
        self.__diskon = {
            1: 0.0,  # Tanpa diskon
            2: 0.1,  # Diskon 10%
            3: 0.15,  # Diskon 15%
            4: 0.2,  # Diskon 20%
            5: 0.25  # Diskon 25%
        }

    def hitung_diskon(self, jumlah_pesan):
        if jumlah_pesan >= 5:
            return self.__diskon[5]
        elif jumlah_pesan == 4:
            return self.__diskon[4]
        elif jumlah_pesan == 3:
            return self.__diskon[3]
        elif jumlah_pesan == 2:
            return self.__diskon[2]
        else:
            return self.__diskon[1]


class AnandaCoffee:
    def __init__(self):
        self.__menu = {
            "a": {"nama": "ES Kopi Susu", "harga": 11000},
            "b": {"nama": "ES Kopi Coklat", "harga": 12000},
            "c": {"nama": "ES Kopi Hitam", "harga": 11000},
            "d": {"nama": "Ice Americano", "harga": 14000}
        }

    def hitung_total_harga(self, pesanan, jumlah):
        if pesanan in self.__menu:
            harga = self.__menu[pesanan]["harga"]
            total_harga = harga * jumlah
            return total_harga
        else:
            return None

    def cetak_pesanan(self, pesanan, jumlah, total_harga, diskon):
        if pesanan in self.__menu:
            nama = self.__menu[pesanan]["nama"]
            print("Ananda Coffee")
            print("--------------")
            print("Pesanan:", nama)
            print("Jumlah:", jumlah)
            print("Total Harga:", total_harga)
            print("Diskon:", diskon * 100, "%")
            print("--------------")


pilihan = "y"
ananda_coffee = AnandaCoffee()
diskon = Diskon()

while pilihan == "y":
    print("""
    ==============================
    
    Ananda Coffee
    List Menu Minuman Kopi
 
    ==============================
    A. ES Kopi Susu : Rp 11.000
    B. ES Kopi Coklat : Rp 12.000
    C. ES Kopi Hitam : Rp 11.000
    D. Ice Americano : Rp 14.000
    ==============================
    """)
    pesan = input("Masukkan kode menu kopi yang dipilih: ")
    jumlah_pesan = int(input("Masukkan jumlah pesanan: "))

    total_harga = ananda_coffee.hitung_total_harga(pesan, jumlah_pesan)
    diskon_persen = diskon.hitung_diskon(jumlah_pesan)
    diskon_harga = total_harga * diskon_persen
    total_harga_diskon = total_harga - diskon_harga

    if total_harga is not None:
        ananda_coffee.cetak_pesanan(pesan, jumlah_pesan, total_harga_diskon, diskon_persen)
    else:
        print("Menu tidak tersedia.")

    pilihan = input("Apakah Anda ingin memesan lagi? (y/n): ")