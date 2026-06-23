import time

def slow(text, delay=0.03):
    """Menampilkan teks perlahan agar terasa lembut."""
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def tulis_jurnal(isi):
    """Menyimpan refleksi ke file jurnal."""
    with open("jurnal_diri.txt", "a", encoding="utf-8") as f:
        f.write(isi + "\n")

def jeda():
    input("\n(tekan Enter untuk melanjutkan...)")

def pembuka():
    slow("🌙 Selamat datang di ‘Perjalanan Menuju Ketenangan Diri’ 🌙\n")
    slow("Kamu tidak sedang bermain untuk menang...")
    slow("Kamu sedang berjalan... untuk mengenali dirimu sendiri.")
    jeda()

def bab1_kesunyian():
    slow("\n🍃 Bab 1: Kesunyian")
    slow("Kamu berada di tempat yang sepi. Hanya ada angin dan gema napasmu sendiri.")
    slow("Tapi... dalam kesunyian ini, kamu merasa aman — seperti dunia berhenti sebentar agar kamu bisa bernapas.")
    slow("\nSuara lembut berbicara dari dalam dirimu...")

    slow("\"Sudah lama kamu tidak benar-benar diam, ya?\"")
    jawab = input("Apa yang kamu rasakan saat diam tanpa gangguan apa pun? ").strip()
    tulis_jurnal(f"[Bab 1 - Kesunyian] {jawab}")
    slow("\nKadang diam membawa kita bukan pada kehilangan, tapi pada pemahaman.")
    jeda()

def bab2_luka():
    slow("\n💔 Bab 2: Luka")
    slow("Kamu berjalan melewati dinding kaca yang retak. Setiap retakan memantulkan kenangan.")
    slow("Ada rasa sakit di sana — tapi juga kejujuran.")
    slow("\nSuara batinmu berkata pelan:")
    slow("\"Tidak apa-apa. Luka itu tidak membuatmu rusak. Ia hanya tanda bahwa kamu pernah berani mencintai.\"")

    jawab = input("\nHal apa yang masih kamu rasakan sakit jika teringat? ").strip()
    tulis_jurnal(f"[Bab 2 - Luka] {jawab}")
    slow("\nAir mata boleh jatuh. Tapi lihatlah — kaca itu tidak hancur. Ia tetap berdiri, dan memantulkan cahaya.")
    jeda()

def bab3_penerimaan():
    slow("\n🌿 Bab 3: Penerimaan")
    slow("Kamu tiba di taman luas. Rumput bergoyang pelan. Matahari hangat menyentuh pipimu.")
    slow("Kamu duduk di sana, menatap langit. Hati terasa lebih ringan dari sebelumnya.")
    slow("\nSuara batin itu kembali berbicara:")
    slow("\"Kamu tidak perlu menjadi versi sempurna dari dirimu. Cukup jadi seseorang yang terus berusaha lembut.\"")

    jawab = input("\nHal apa yang ingin kamu maafkan dari dirimu hari ini? ").strip()
    tulis_jurnal(f"[Bab 3 - Penerimaan] {jawab}")
    slow("\nKamu memejamkan mata. Rasanya seperti beratmu perlahan berkurang.")
    jeda()

def bab4_cahaya():
    slow("\n✨ Bab 4: Cahaya")
    slow("Langit mulai berwarna keemasan. Kamu berdiri di tepi bukit, memandang jauh.")
    slow("Kamu sadar... perjalanan ini bukan untuk menemukan siapa kamu seharusnya, tapi untuk mengingat siapa kamu sebenarnya.")
    slow("\nSuara batin itu tersenyum di dalam dirimu.")
    slow("\"Kamu sudah berjalan sejauh ini. Dan aku bangga padamu.\"")

    jawab = input("\nSebutkan satu hal kecil yang membuatmu bersyukur hari ini: ").strip()
    tulis_jurnal(f"[Bab 4 - Cahaya] {jawab}")
    slow(f"\nKamu tersenyum... karena {jawab} adalah cahaya kecil yang menuntunmu pulang.")
    jeda()

def penutup():
    slow("\n🌾 Penutup: Kembali ke Dalam Diri")
    slow("Kamu menarik napas dalam-dalam. Tidak ada lagi yang harus dikejar.")
    slow("Kamu cukup. Kamu layak. Dan kamu damai.")
    slow("\nTerima kasih sudah berjalan sejauh ini bersamaku 🌙")
    slow("Semua jawabanmu tersimpan di file 'jurnal_diri.txt' — bacalah kembali kapan pun kamu ingin mengenal dirimu.")
    slow("\n🕊️ Selesai 🕊️")

# Jalankan game
pembuka()
bab1_kesunyian()
bab2_luka()
bab3_penerimaan()
bab4_cahaya()
penutup()

