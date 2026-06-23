import pygame
import random

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Sederhana Python - Level Sulit")

# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Karakter pemain
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 5

# Musuh
enemy_size = 50
enemy_speed = 5
num_enemies = 5
enemies = []
for _ in range(num_enemies):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(-300, -50)
    enemies.append([x, y])

# Skor
score = 0
font = pygame.font.SysFont(None, 36)

# Nyawa pemain
lives = 20

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # FPS 60
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Gerakkan musuh
    for enemy in enemies:
        enemy[1] += enemy_speed
        enemy[0] += random.choice([-1, 0, 1])  # sedikit zig-zag
        if enemy[1] > HEIGHT:
            enemy[1] = random.randint(-300, -50)
            enemy[0] = random.randint(0, WIDTH - enemy_size)
            score += 1
            # tingkatkan kecepatan setiap 5 skor
            if score % 5 == 0:
                enemy_speed += 0.5

    # Gambar pemain dan musuh
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Cek tabrakan
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            lives -= 1
            enemy[1] = random.randint(-300, -50)
            enemy[0] = random.randint(0, WIDTH - enemy_size)
            if lives == 0:
                running = False

    # Tampilkan skor dan nyawa
    score_text = font.render(f"Skor: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Nyawa: {lives}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    # Update layar
    pygame.display.flip()

pygame.quit()
print(f"Game over! Skormu: {score}")


