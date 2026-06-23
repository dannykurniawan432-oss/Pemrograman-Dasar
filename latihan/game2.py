import time

def slow_print(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.02)
    print()

slow_print("=== Petualangan di Gua Gelap ===")
slow_print("Kamu terbangun di dalam gua misterius yang dingin dan lembap.")
slow_print("Di depanmu ada dua jalan: satu ke kiri yang terang, satu ke kanan yang gelap...")

pilihan1 = input("Mau ke mana? (kiri/kanan): ").lower()

if pilihan1 == "kiri":
    slow_print("Kamu berjalan ke arah cahaya dan menemukan sebuah peti harta karun! 🏆")
    slow_print("Namun, seekor naga besar sedang tidur di dekatnya...")
    pilihan2 = input("Apa yang kamu lakukan? (ambil/kabur/intip): ").lower()

    if pilihan2 == "ambil":
        slow_print("🔥 Naga bangun dan membakarmu! Kamu menjadi abu... Game over!")
    elif pilihan2 == "kabur":
        slow_print("Kamu berhasil keluar dari gua dengan selamat! Tapi tanpa harta... 😌")
    elif pilihan2 == "intip":
        slow_print("Kamu pelan-pelan mendekat dan melihat bahwa petinya terbuka sedikit.")
        slow_print("Di dalamnya ada sebuah kunci berkilau... mungkin untuk sesuatu?")
        pilihan3 = input("Ambil kunci atau pergi? (ambil/pergi): ").lower()

        if pilihan3 == "ambil":
            slow_print("Kamu mengambil kunci dan kabur sebelum naga terbangun!")
            slow_print("Kamu kembali ke lorong awal, kali ini mencoba jalan kanan...")
            pilihan4 = "kanan"
        else:
            slow_print("Kamu meninggalkan kunci itu dan kembali dengan tangan kosong.")
            pilihan4 = None
    else:
        slow_print("Kamu ragu terlalu lama... naga bangun! 😱")
        slow_print("🔥 Kamu dibakar hidup-hidup! Game over!")
        pilihan4 = None

elif pilihan1 == "kanan":
    slow_print("Kamu masuk ke lorong gelap. Suara air menetes membuat suasana makin tegang.")
    slow_print("Tiba-tiba kamu melihat dua pintu: satu kayu tua, satu batu besar dengan simbol aneh.")
    pilihan4 = input("Masuk pintu mana? (kayu/batu): ").lower()

else:
    slow_print("Kamu hanya berdiri bingung... sampai perlahan gua runtuh di sekitarmu 😢")
    exit()

# Bagian lanjutan (jika memilih jalan kanan atau berhasil ke sana)
if pilihan4 == "kanan" or pilihan4 in ["kayu", "batu"]:
    if pilihan4 == "kayu":
        slow_print("Pintu kayu berderit saat kamu dorong. Di dalamnya ada meja tua dan lilin menyala.")
        slow_print("Di atas meja ada gulungan kertas. Kamu membukanya...")
        slow_print("‘KUNCI EMAS MEMBUKA JALAN MENUJU CAHAYA’ — tulisannya.")
        slow_print("Apakah kamu punya kunci itu? (ya/tidak)")
        jawab = input("> ").lower()

        if jawab == "ya":
            slow_print("Kamu menggunakan kunci itu ke dinding di belakang meja.")
            slow_print("Sebuah pintu rahasia terbuka... dan kamu keluar menuju cahaya matahari! ☀️")
            slow_print("🎉 SELAMAT! Kamu menemukan jalan keluar dan selamat dari gua misterius.")
        else:
            slow_print("Kamu tidak punya kuncinya... gua mulai runtuh! 💥")
            slow_print("Kamu terperangkap selamanya di dalam gua.")
    elif pilihan4 == "batu":
        slow_print("Kamu menyentuh simbol di pintu batu...")
        slow_print("Simbol itu menyala, dan makhluk bayangan muncul dari kegelapan! 👻")
        slow_print("Makhluk itu menatapmu dan berkata, 'Berikan kunci atau nyawamu!'")
        jawab = input("Apa yang kamu lakukan? (beri/lawan/lari): ").lower()

        if jawab == "beri":
            slow_print("Makhluk itu menerima kunci, lalu menghilang... dan pintu terbuka.")
            slow_print("Kamu melangkah keluar ke dunia bebas. Kamu selamat! ✨")
        elif jawab == "lawan":
            slow_print("Kamu mencoba melawan, tapi makhluk itu terlalu kuat... 💀")
        else:
            slow_print("Kamu lari secepat mungkin, tapi makhluk itu mengejarmu...")
            slow_print("...dan akhirnya kamu jatuh ke jurang tanpa dasar 😱")

slow_print("\n=== Akhir Petualangan ===")


