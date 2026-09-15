p = {
    "pangan":{"tempe": 5000, "tahu": 5000, "telur": 2500},
    "minum":{"teh": 5000, "kopi": 6000, "air galon": 10000}
}
while True:
    print("="*60)
    print("STOK TOKO PAK JOKOWY")
    print("1. Tampilkan Seluruh Stock")
    print("2. Tambah Kategori Baru")
    print("3. Hapus Kategori")
    print("4. Ubah Data Kategori")
    print("5. Keluar")
    print("="*60)
    pilih = input("Pilih antara [1-5] : ")
    print("="*60)
    if pilih == "1":
        print("STOK BARANG")
        print(f"{p}")
    elif pilih == "2":
        pb = input("MASUKKAN KATEGORI PRODUK BARU : ").lower()
        p[pb] = {}
        print(f"KATEGORI PRODUK {pb} BERHASIL DITAMBAHKAN")
    elif pilih == "3":
        print("STOK BARANG")
        print(f"{p}")
        ph = input("MASUKKAN NAMA KATEGORI YANG INGIN DI HAPUS : ").lower()
        if ph in p:
            del p[ph]
            print("="*60)
            print(f"KATEGOIR {ph} BERHASIL DI HAPUS")
    elif pilih == "4":
        print("STOK BARANG")
        print(f"{p}")
        print("="*60)
        pu = input("MASUKKAN NAMA KATEGORI YANG MAU DI UBAH : ").lower()
        if pu in p:
            np = input("MASUKKAN NAMA BARANG : ").lower()
            try:
                hp = int(input("Masukkan harga barang : "))
                p[pu][np]= hp
                print("DATA BERHASIL DI PERBARUI")
            except ValueError:
                print("HARGA HARUS BERUAP ANGKA")
        else:
            print("KATEGORI TIDAK DITEMUKAN")
    elif pilih == "5":
        print("GOODBYE")
        break
