import random
import time
import os

# ===== EXCEPTION HANDLING =====
try:
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            highscore = int(f.read())
    else:
        highscore = 5

except:
    highscore = 0


# ===== DATA STRUCTURE =====
snake = [(3, 5), (2, 5), (1, 5)]   # posisi ular (x,y)
direction = "RIGHT" # diawal game ular bergerak ke kiri
food = (10, 6) # titik (x,y)
score = 0 # score mulai dari 0
width = 25 # lebar
height = 15 # tinggi


# ===== FUNGSI =====
def spawn_food():
    return (random.randint(5, width - 5), random.randint(3, height - 5))
# posisi makanan acak posisi (x,y)


def draw_board(): 
    print("\033c", end="")
    # membersihkan layar terminal sebelum menggambar ulang papan game.
    for y in range(height):
        for x in range(width):

            # === Kepala Ular ===
            if (x, y) == snake[0]:
                print("=", end="")  

            # === Badan Ular ===
            elif (x, y) in snake[1:]:
                print("+", end="")

            # === Makanan ===
            elif (x, y) == food:
                print("x", end="")

        
            # === Dinding ===
            elif y == 0:
                 print("^", end="")          # Atas
            elif y == height - 1:
                 print("=", end="")          # Bawah
            elif x == 0:
                 print("|", end="")          # Kiri
            elif x == width - 1:
                 print("|", end="")          # Kanan



            # === Ruang kosong ===
            else:
                print(" ", end="")
        print()

    print(f"Score: {score} | Highscore: {highscore}")
    print("Gunakan: U D L R  untuk gerak. (Tekan ENTER setelah mengetik)")


def move_snake():
    global score, food, highscore

    head_x, head_y = snake[0]

    # ===== LOGIKA PERGERAKAN =====
    if direction == "RIGHT":
        new_head = (head_x + 1, head_y)
    elif direction == "LEFT":
        new_head = (head_x - 1, head_y)
    elif direction == "UP":
        new_head = (head_x, head_y - 1)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 1)

    # ===== GAME OVER: Nabrak tembok =====
    if (new_head[0] in [0, width - 1]) or (new_head[1] in [0, height - 1]):
        return False

    # ===== GAME OVER: Nabrak badan sendiri =====
    if new_head in snake:
        return False

    snake.insert(0, new_head)

    # ===== MAKAN FOOD =====
    if new_head == food:
        score += 1

        if score > highscore:
            highscore = score
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
    
        food = spawn_food()
    else:
        snake.pop()

    return True


# ===== GAME LOOP =====
while True:
    draw_board()

    command = input("Input: ").upper()

    if command == "U" and direction != "DOWN":
        direction = "UP"
    elif command == "D" and direction != "UP":
        direction = "DOWN"
    elif command == "L" and direction != "RIGHT":
        direction = "LEFT"
    elif command == "R" and direction != "LEFT":
        direction = "RIGHT"

    running = move_snake()

    if not running:
        print("\033c", end="")
        print("GAME OVER!")
        print(f"Final Score: {score}")
        print(f"Highscore: {highscore}")
        break

    time.sleep(0.2)
