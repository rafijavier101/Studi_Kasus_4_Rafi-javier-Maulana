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
ini adalah kode untuk menambahkan kategori pada dictionary

<img width="348" height="170" alt="terminal 2 sc4" src="https://github.com/user-attachments/assets/8ad1cd57-4f85-40bd-932f-b8fce9cbe143" />

elif pilih == "3":

        print("STOK BARANG")
        print(f"{p}")
        ph = input("MASUKKAN NAMA KATEGORI YANG INGIN DI HAPUS : ").lower()
        if ph in p:
            del p[ph]
            print("="*60)
            print(f"KATEGOIR {ph} BERHASIL DI HAPUS")
ini adalah untuk menghapus kategori yang sudah ada

<img width="790" height="209" alt="terminal 3sc4" src="https://github.com/user-attachments/assets/a9dd29b5-20b9-4ea1-95f5-f87e596d2b54" />

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
ini adalah kode untuk mengubah data yang ada di dalam kategori

<img width="784" height="457" alt="terminal 4sc4" src="https://github.com/user-attachments/assets/8e20a78f-77be-483a-aa77-6b25772f4739" />

 elif pilih == "5":
 
        print("GOODBYE")
        break
ini adalah kode untuk mengakhiri program

<img width="366" height="164" alt="terminal 5sc4" src="https://github.com/user-attachments/assets/7ba48638-4f9f-405a-9aca-b0f7ac7bbc9c" />







