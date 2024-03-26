def hitung_diskon(total_belanja):
    if total_belanja >= 250000:
        diskon = total_belanja * 50 / 100
        return diskon
    else:
        return None

total_belanja = float(input("Masukkan total belanja Anda: Rp. "))
diskon = hitung_diskon(total_belanja)

if diskon is not None:
    print("Anda mendapatkan diskon sebesar Rp.", diskon)
else:
    print("Total belanjaan Anda adalah Rp.", total_belanja)
    print("Maaf, Anda tidak mendapatkan diskon karena total belanjaan tidak mencapai Rp. 250.000.")
