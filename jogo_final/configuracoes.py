import pygame
from pygame.math import Vector2 as vector
from sys import exit

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
TILE_SIZE = 32
ANIMATION_SPEED = 6
BATTLE_OUTLINE_WIDTH = 4

COLORS = {
    'white': '#f4fefa',
    'pure white': '#ffffff',
    'dark': '#2b292c',
    'light': '#c8c8c8',
    'gray': '#3a373b',
    'gold': '#ffd700',
    'light-gray': '#4b484d',
    'fire': '#f8a060',
    'water': '#50b0d8',
    'plant': '#64a990',
    'black': '#000000',
    'red': '#f03131',
    'blue': '#66d7ee'
}

WORLD_LAYERS = {
    'fundo': 0,
    'principal': 1,
    'cima': 2
}

BATTLE_POSITIONS = {
}

BATTLE_LAYERS = {
}

BATTLE_CHOICES = {
}