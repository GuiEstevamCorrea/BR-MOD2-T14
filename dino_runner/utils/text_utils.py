import pygame
from dino_runner.utils.constants import (
    FONT_COLOR_BLACK,
    FONT_SIZE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH, 
    FONT_STYLE
)


def draw_message_component(
        message,
        screen,
        font_color=FONT_COLOR_BLACK,
        font_size=FONT_SIZE,
        pos_y_center=SCREEN_HEIGHT // 2,
        pos_x_center=SCREEN_WIDTH // 2,
):
    font = pygame.font.Font(FONT_STYLE, FONT_SIZE)
    # Cor do score, Tamanho da fonte
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    # Posição do Score
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)