# Studi_Kasus_4_Rafi-javier-Maulana
<img width="1280" height="800" alt="sc4_code" src="https://github.com/user-attachments/assets/a2c220fa-8e17-4c33-be84-5ee0b7303642" />

  p = {
  
      "pangan":{"tempe": 5000, "tahu": 5000, "telur": 2500},
      "minum":{"teh": 5000, "kopi": 6000, "air galon": 10000}
      }    
ini adalah kode dictionary untuk data awal / stok awal toko

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
ini adalah kode untuk menu utama

<img width="346" height="153" alt="menu sc4" src="https://github.com/user-attachments/assets/658de28e-f431-4531-9611-137d6b576589" />

if pilih == "1":

        print("STOK BARANG")
        print(f"{p}")
ini adalah kode untuk menampilkan seluruh stok yang ada ditoko jika user memilih pilihan 1 pada menu

<img width="645" height="182" alt="terminal 1 sc4" src="https://github.com/user-attachments/assets/0f0583bf-e5bd-42ae-88e6-930d3a0f2b94" />

elif pilih == "2":

        pb = input("MASUKKAN KATEGORI PRODUK BARU : ").lower()
        p[pb] = {}
        print(f"KATEGORI PRODUK {pb} BERHASIL DITAMBAHKAN")



