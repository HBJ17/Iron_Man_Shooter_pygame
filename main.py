# main.py
import pygame, random
from settings import *
from game.explosion import create_explosion, explosions, update_explosions
from game.utils import draw_health

# Load images and sounds
player_img = pygame.transform.scale(pygame.image.load(PLAYER_IMG), (60, 60))
enemy_img = pygame.transform.scale(pygame.image.load(ENEMY_IMG), (50, 50))
bullet_img = pygame.transform.scale(pygame.image.load(BULLET_IMG), (30, 30))
bg_img = pygame.transform.scale(pygame.image.load(BG_IMG), (W, H))

shoot_sound = pygame.mixer.Sound(SHOOT_SOUND)
explosion_sound = pygame.mixer.Sound(EXPLOSION_SOUND)

# Player
player = player_img.get_rect(center=(60, H//2))
bullets, enemies = [], []
score, spawn_time, player_health = 0, 0, 100
game_over = False
font = pygame.font.SysFont(None, 40)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            b = bullet_img.get_rect(center=(player.right, player.centery))
            bullets.append(b)
            shoot_sound.play()

    if game_over:
        win.fill((10, 0, 20))
        t = font.render("GAME OVER", True, (255, 0, 0))
        s = font.render(f"Final Score: {score}", True, (255, 255, 255))
        r = font.render("Press R to Restart", True, (255, 255, 255))
        win.blit(t, (W//2 - 90, H//2 - 50))
        win.blit(s, (W//2 - 120, H//2 - 10))
        win.blit(r, (W//2 - 150, H//2 + 30))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            bullets, enemies, explosions[:] = [], [], []
            score, player_health, game_over = 0, 100, False
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < H:
        player.y += 5

    spawn_time += 1
    if spawn_time > 40:
        y = random.randint(0, H - 50)
        e = enemy_img.get_rect(topleft=(W, y))
        enemies.append(e)
        spawn_time = 0

    for b in bullets: b.x += 10
    for e in enemies: e.x -= 4

    for b in bullets[:]:
        for e in enemies[:]:
            if b.colliderect(e):
                create_explosion(e.x, e.y)
                bullets.remove(b)
                enemies.remove(e)
                explosion_sound.play()
                score += 1
                break

    bullets = [b for b in bullets if b.x < W]
    enemies = [e for e in enemies if e.x > -50]

    for e in enemies[:]:
        if e.colliderect(player):
            player_health -= 25
            create_explosion(e.x, e.y)
            enemies.remove(e)
            explosion_sound.play()
            if player_health <= 0:
                game_over = True

    update_explosions()

    win.blit(bg_img, (0, 0))
    win.blit(player_img, player)
    for b in bullets: win.blit(bullet_img, b)
    for e in enemies: win.blit(enemy_img, e)

    for ex in explosions:
        surf = pygame.Surface((ex["size"], ex["size"]), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 200, 50, ex["alpha"]), (ex["size"]//2, ex["size"]//2), ex["size"]//2)
        win.blit(surf, (ex["x"], ex["y"]))

    score_txt = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(score_txt, (10, 35))
    draw_health(player_health)
    pygame.display.update()

pygame.quit()
