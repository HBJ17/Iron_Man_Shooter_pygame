# settings.py
import pygame

# Screen size
W, H = 720, 480

pygame.init()
try:
    pygame.mixer.init()
except:
    pass

# Window
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Iron Man Shooter")
clock = pygame.time.Clock()

# Assets folder paths
PLAYER_IMG = "assets/player.png"
ENEMY_IMG = "assets/enemy.png"
BULLET_IMG = "assets/bullet.png"
BG_IMG = "assets/Bg.jpg"
SHOOT_SOUND = "assets/Shoot.mp3"
EXPLOSION_SOUND = "assets/Explosion.mp3"
