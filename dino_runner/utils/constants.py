import os

import pygame

# Global constants
TITLE = "Warrior Runner "
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

#text
FONT_STYLE = "freesansbold.ttf"
FONT_SIZE = 22
FONT_COLOR_BLACK = (0, 0, 0) #Black
FONT_COLOR_WHITE = (255, 255, 255) #White



# Assets constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Dino/Warrior_Death_11_new.png"))

# Run
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/Warrior_Run_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/Warrior_Run_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/Warrior_Run_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/Warrior_Run_4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/Warrior_Run_5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/Warrior_Run_6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/Warrior_Run_7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/Warrior_Run_8.png")),
]
RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunShield2.png")),
]
RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer2.png")),
]

# Duck
DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/Warrior-Slide_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/Warrior-Slide_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/Warrior-Slide_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/Warrior-Slide_4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/Warrior-Slide_5.png")),
]
DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckShield2.png")),
]
DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer2.png")),
]

# Jump
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump/Warrior_Jump_1.png"))
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump/Warrior_Fall_3.png"))
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpShield.png")
)
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpHammer.png")
)

# Obstacles
SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/fire_column_medium_5_small.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/fire_column_medium_5_small.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/fire_column_medium_5_small.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/fire_column_medium_5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/fire_column_medium_5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/fire_column_medium_5.png")),
]
BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/FB001.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/FB002.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/FB003.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/FB004.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/FB005.png")),
]

# Doodads
CLOUD = pygame.image.load(os.path.join(IMG_DIR, "Other/Cloud.png"))

# Power ups
SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Other/Shield.png"))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Other/Hammer.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, "Other/Track.png"))
HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/SmallHeart.png"))

DEFAULT_TYPE = "default"
