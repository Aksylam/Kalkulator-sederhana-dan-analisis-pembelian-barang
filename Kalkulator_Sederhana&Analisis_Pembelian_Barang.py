#data
id_pelanggan = (input("Nama pelanggan "))
jumlah_uang = float(input("Jumlah uang yang dibayarkan(Rp) "))

print ("------ Daftar barang dibeli------\n" )

print ("barang ke-1")
id_barang1 = (input("Masukan nama barang disini: "))
jumlah_barang1 = int(input("Masukkan jumlah barang dibeli disini: "))
harga_satuan1 = float(input("Masukkan harga barang satuan dibeli: "))

print ("\nbarang ke-2")
id_barang2 = (input("Masukan nama barang disini: "))
jumlah_barang2 = int(input("Masukkan jumlah barang dibeli disini: "))
harga_satuan2 = float(input("Masukkan harga barang satuan dibeli: " ))

print ("\nbarang ke-3")
id_barang3 = (input("Masukan nama barang disini: "))
jumlah_barang3 = int(input("Masukkan jumlah barang dibeli disini: "))
harga_satuan3 = float(input("Masukkan harga barang satuan dibeli: "))

#logika kalkulator
total_harga1 = jumlah_barang1*harga_satuan1
total_harga2 = jumlah_barang2*harga_satuan2
total_harga3 = jumlah_barang3*harga_satuan3

total_belanja = total_harga1+total_harga2+total_harga3

#print struk
print ("\n------Selamat Datang di Toko Alat Tulis Al-tahzan------")
print (f"selamat datang bapak/ibu {id_pelanggan}")
print (f"Uang Tunai: {jumlah_uang:,.2f}")
print ("\n" + "="*40)
print ("\n------Struk pembelian------")
print ("\n" + "="*40)
print (f"{id_barang1:.<15}{jumlah_barang1} @ Rp {harga_satuan1:,.0f} = Rp {total_harga1:,.2f}")
print (f"{id_barang2:.<15}{jumlah_barang2} @ Rp {harga_satuan2:,.0f} = Rp {total_harga2:,.2f}")
print (f"{id_barang3:.<15}{jumlah_barang3} @ Rp {harga_satuan3:,.0f} = Rp {total_harga3:,.2f}")
print ("\n" + "="*40)
print (f"Total belanjaan = Rp {total_belanja:,.2f}")
print ("Jumlah uang yang diterima = Rp", jumlah_uang)
if jumlah_uang < total_belanja:
    print ("Uang anda tidak cukup")
elif jumlah_uang >= total_belanja:
    print (f"kembalian = Rp {jumlah_uang-total_belanja:,.2f}")
print ("Terimakasih telah berbelanja!!!")
print ("\n" + "="*40)