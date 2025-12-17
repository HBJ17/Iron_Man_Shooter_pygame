# game/utils.py
import pygame
from settings import win

def draw_health(health):
    pygame.draw.rect(win, (255, 0, 0), (10, 10, 100, 15))
    pygame.draw.rect(win, (0, 255, 0), (10, 10, health, 15))
