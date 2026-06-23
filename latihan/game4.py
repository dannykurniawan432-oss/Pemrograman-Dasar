import time

def slow(text, delay=0.02):
    """Menampilkan teks perlahan agar terasa lembut."""
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def jeda():
    input("\n(tekan Enter untuk melanjutkan...)")

def tanya(prompt, opsi):
    """Menanyakan pertanyaan dan memastikan jawaban valid."""
    while True:
        jawaban = input(prompt + f" {opsi}: ").lower().strip()
        if jawaban in opsi:
            return jawaban
        else:
            print(f"Pilihan tidak valid. Silakan pilih {opsi}.")

def main():
    slow("🌙 Selamat datang di Refleksi Kesehatan Mental 🌙\n")
    slow("Tujuan permainan ini adalah untuk membantu kamu memahami kondisi emosional dan mentalmu saat ini.\n")
    jeda()

    skor_stres = 0
    skor_cemas = 0
    skor_resiliensi = 0

    # Pertanyaan 1
    q1 = tanya("Seberapa sering kamu merasa cemas atau gelisah dalam seminggu terakhir?", ["sering", "kadang", "jarang"])
    if q1 == "sering":
        skor_cemas += 2
    elif q1 == "kadang":
        skor_cemas += 1

    # Pertanyaan 2
    q2 = tanya("Apakah kamu bisa tidur nyenyak sebagian besar malam?", ["ya", "tidak"])
    if q2 == "tidak":
        skor_stres += 2
    else:
        skor_resiliensi += 1

    # Pertanyaan 3
    q3 = tanya("Apakah kamu punya kegiatan yang membuatmu rileks, seperti berjalan, meditasi, atau membaca?", ["ya", "tidak"])
    if q3 == "ya":
        skor_resiliensi += 2
    else:
        skor_stres += 1

    # Pertanyaan 4
    q4 = tanya("Saat menghadapi masalah, apakah kamu biasanya berbicara dengan orang yang kamu percaya?", ["ya", "tidak"])
    if q4 == "ya":
        skor_resiliensi += 1
    else:
        skor_stres += 1

    # Pertanyaan 5
    q5 = tanya("Seberapa sering kamu merasa sulit menikmati hal-hal yang biasanya menyenangkan?", ["sering", "kadang", "jarang"])
    if q5 == "sering":
        skor_stres += 2
    elif q5 == "kadang":
        skor_stres += 1

    # Pertanyaan 6
    q6 = tanya("Apakah kamu mudah tersulut emosi atau merasa frustrasi dengan cepat?", ["ya", "tidak"])
    if q6 == "ya":
        skor_cemas += 1
    else:
        skor_resiliensi += 1

    # Ringkasan dan tips
    slow("\n=== Hasil Refleksi ===")
    slow(f"Skor Stres: {skor_stres}, Skor Cemas: {skor_cemas}, Skor Resiliensi: {skor_resiliensi}\n")

    if skor_stres >= 5 or skor_cemas >= 4:
        slow("⚠️ Kamu tampak mengalami tekanan emosional atau kecemasan yang cukup tinggi.")
        slow("Tips: coba lakukan teknik pernapasan, meditasi, berjalan di alam, atau berbicara dengan orang yang kamu percaya.")
    elif skor_stres >= 3 or skor_cemas >= 2:
        slow("😊 Kamu mengalami tekanan ringan, tapi tetap perlu memperhatikan kesehatan mentalmu.")
        slow("Tips: alokasikan waktu untuk diri sendiri dan lakukan aktivitas yang menenangkan.")
    else:
        slow("🌸 Kamu terlihat cukup stabil secara mental. Tetap pertahankan kebiasaan positifmu!")
        slow("Tips: refleksi diri rutin dan menjaga pola tidur & aktivitas tetap penting.")

    if skor_resiliensi >= 4:
        slow("\n✨ Kamu menunjukkan ketahanan yang baik. Kemampuanmu untuk menghadapi stres dan tetap tenang cukup tinggi.")

    slow("\nTerima kasih telah melakukan refleksi ini. Semoga bermanfaat untuk perjalanan kesehatan mentalmu 🌿")
    jeda()

if __name__ == "__main__":
    main()