
print("=== DATA OBAT APOTEK ===")

print("1. Paracetamol")
print("2. Amoxicillin")
print("3. Antasida")
print("4. Ibuprofen")
print("5. CTM")
print("6. Vitamin C")
print("7. Betadine")
print("8. Oralit")
print("9. Cetirizine")
print("10. Ambroxol")

pilihan = int(input("Pilih nomor obat: "))

if pilihan == 1:
    obat = "Paracetamol"
    harga = 5000
    stok = 20
elif pilihan == 2:
    obat = "Amoxicillin"
    harga = 12000
    stok = 15
elif pilihan == 3:
    obat = "Antasida"
    harga = 4000
    stok = 0
elif pilihan == 4:
    obat = "Ibuprofen"
    harga = 8000
    stok = 12
elif pilihan == 5:
    obat = "CTM"
    harga = 3000
    stok = 10
elif pilihan == 6:
    obat = "Vitamin C"
    harga = 6000
    stok = 25
elif pilihan == 7:
    obat = "Betadine"
    harga = 10000
    stok = 8
elif pilihan == 8:
    obat = "Oralit"
    harga = 2500
    stok = 0
elif pilihan == 9:
    obat = "Cetirizine"
    harga = 7000
    stok = 18
elif pilihan == 10:
    obat = "Ambroxol"
    harga = 9000
    stok = 14
else:
    obat = ""
    harga = 0
    stok = 0

if pilihan >= 1 and pilihan <= 10:
    print("\nNama obat:", obat)
    print("Harga obat: Rp", harga)
    print("Stok obat:", stok)

    if stok > 0:
        print("Keterangan: Obat tersedia")
    else:
        print("Keterangan: Stok obat habis")
else:
    print("Pilihan tidak tersedia")
