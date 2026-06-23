import turtle
import random
import time
import os

# Fungsi untuk menyimpan skor ke file teks (menyimpan data teks)
def save_score(score):
    try:
        with open("snake_score.txt", "w") as file:
            file.write(f"Skor Tertinggi: {score}\n")
        print("Skor berhasil disimpan!")
    except Exception as e:
        print(f"Error saat menyimpan skor: {e}")

# Fungsi untuk memuat skor dari file teks (exception handling untuk file tidak ada)
def load_score():
    try:
        if os.path.exists("snake_score.txt"):
            with open("snake_score.txt", "r") as file:
                data = file.read()
                # Menggunakan operator string untuk ekstrak skor
                if "Skor Tertinggi:" in data:
                    score_str = data.split(": ")[1].strip()
                    return int(score_str)
        return 0
    except Exception as e:
        print(f"Error saat memuat skor: {e}")
        return 0

# Fungsi untuk menggambar persegi (untuk ular dan makanan)
def draw_square(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):  # Logika perulangan untuk menggambar persegi
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()

# Fungsi utama game
def snake_game():
    # Setup layar
    screen = turtle.Screen()
    screen.title("Game Ular Bertahap")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.tracer(0)  # Matikan tracer untuk update manual

    # Ular sebagai struktur data (list of tuples untuk posisi)
    snake = [(0, 0)]  # Struktur data: list
    direction = "right"  # Arah awal
    food = (random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)  # Posisi makanan acak
    score = 0
    high_score = load_score()  # Muat skor tertinggi
    speed = 0.3  # Kecepatan awal (lebih lambat dari sebelumnya)
    level = 1  # Level awal
    level_targets = {1: 5, 2: 10, 3: 15}  # Target skor per level (dict sebagai struktur data)
    max_level = max(level_targets.keys())  # Level maksimal

    # Fungsi untuk mengubah arah (logika kondisional untuk mencegah balik arah)
    def change_direction(new_dir):
        nonlocal direction
        opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
        if new_dir != opposites.get(direction, ""):
            direction = new_dir

    # Fungsi untuk mengurangi kecepatan (membuat lebih lambat)
    def decrease_speed():
        nonlocal speed
        if speed < 0.5:  # Batas maksimal lambat (opsional, agar tidak terlalu lambat)
            speed += 0.05  # Operator penjumlahan

    # Bind keyboard
    screen.listen()
    screen.onkey(lambda: change_direction("up"), "Up")
    screen.onkey(lambda: change_direction("down"), "Down")
    screen.onkey(lambda: change_direction("left"), "Left")
    screen.onkey(lambda: change_direction("right"), "Right")
    screen.onkey(decrease_speed, "s")  # Tombol "S" untuk kurangi kecepatan

    # Loop utama game (logika perulangan)
    while True:
        screen.update()
        time.sleep(speed)

        # Hitung posisi kepala baru berdasarkan arah (operator aritmatika)
        head_x, head_y = snake[0]
        if direction == "up":
            head_y += 20
        elif direction == "down":
            head_y -= 20
        elif direction == "left":
            head_x -= 20
        elif direction == "right":
            head_x += 20

        # Cek tabrakan dengan dinding (logika kondisional)
        if abs(head_x) > 280 or abs(head_y) > 280:
            break  # Game over

        # Cek tabrakan dengan tubuh sendiri (logika kondisional dan perulangan)
        for segment in snake[1:]:
            if (head_x, head_y) == segment:
                screen.update()
                time.sleep(0.3)
                return      # Game over

        # Tambah kepala baru
        snake.insert(0, (head_x, head_y))

        # Cek apakah makan makanan (logika kondisional)
        if (head_x, head_y) == food:
            score += 1  # Operator penjumlahan
            food = (random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)
        else:
            snake.pop()  # Hapus ekor jika tidak makan

        # Cek apakah level selesai (logika kondisional baru)
        if level in level_targets and score >= level_targets[level]:
            # Tampilkan pesan level selesai
            turtle.goto(0, 0)
            turtle.write(f"Level {level} Selesai! Skor: {score}", align="center", font=("Arial", 20, "normal"))
            time.sleep(2)  # Jeda 2 detik
            
            # Tanya lanjut atau tidak (sederhana, gunakan input konsol atau tombol)
            # Untuk sederhana, gunakan turtle untuk pesan dan tunggu input
            turtle.goto(0, -50)
            turtle.write("Tekan 'Y' untuk lanjut level, 'N' untuk keluar", align="center", font=("Arial", 16, "normal"))
            
            # Loop kecil untuk tunggu input (logika perulangan)
            continue_game = None
            while continue_game is None:
                screen.update()
                time.sleep(0.1)
                # Simulasi input sederhana (dalam turtle, kita pakai onkey untuk Y/N)
                def set_continue():
                    nonlocal continue_game
                    continue_game = True
                def set_exit():
                    nonlocal continue_game
                    continue_game = False
                screen.onkey(set_continue, "y")
                screen.onkey(set_exit, "n")
                # Tunggu sampai pemain tekan Y atau N
            
            if not continue_game:
                break  # Keluar game
            
            # Jika lanjut, naik level dan tingkatkan tantangan
            level += 1  # Operator penjumlahan
            if level > max_level:
                turtle.clear()
                turtle.goto(0, 0)
                turtle.write("Selamat! Semua Level Selesai!", align="center", font=("Arial", 24, "normal"))
                break
            speed = max(0.1, speed - 0.05)  # Kurangi speed (cepatkan sedikit per level), tapi minimal 0.1
            # Bersihkan pesan dan lanjut
            turtle.clear()

        # Gambar ulang layar
        turtle.clear()
        # Gambar ular (perulangan untuk setiap segmen)
        for segment in snake:
            draw_square(segment[0], segment[1], "green")
        # Gambar makanan
        draw_square(food[0], food[1], "red")

        # Tampilkan skor dan level (operator string)
        turtle.penup()
        turtle.goto(-280, 260)
        turtle.pencolor("white")
        turtle.write(f"Level: {level}  Skor: {score}  Target: {level_targets.get(level, 'N/A')}  Skor Tertinggi: {high_score}", font=("Arial", 14, "normal"))

    # Game over
    turtle.goto(0, 0)
    turtle.write("Game Over!", align="center", font=("Arial", 24, "normal"))

    # Simpan skor jika lebih tinggi (logika kondisional)
    if score > high_score:
        save_score(score)

    screen.mainloop()

# Jalankan game
if __name__ == "__main__":
    snake_game()





 
