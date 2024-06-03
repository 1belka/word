import pygame
import sys
from game_logic import check_word
from const import *
import subprocess
import tkinter as tk



pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Угадай слово")

font = pygame.font.Font(None, FONT_SIZE)

SECRET_WORD = random.choice(WORD_LIST)
print("SECRET_WORD:", SECRET_WORD)

guesses = []
current_guess = ""
game_won = False
game_lost = False


def draw():
    screen.fill(WHITE)
    
    for i, guess in enumerate(guesses):
        display_guess(guess, i)
        
    if not game_won and not game_lost:
        display_guess(current_guess, len(guesses), is_current=True)
    
    if game_won:
        subprocess.run([sys.executable, "win.py"])
        sys.exit()
#        display_message("WIN!")
    elif game_lost:
        subprocess.run([sys.executable, "lose.py"])
        sys.exit()
#       display_message(f"You lose. Word: {SECRET_WORD}")
    
    pygame.display.flip()

def display_guess(guess, row, is_current=False):
    for i, letter in enumerate(guess.ljust(WORD_LENGTH)):
        color = GREY
        if not is_current:
            color = YELLOW if letter in SECRET_WORD and letter != SECRET_WORD[i] else color
            color = GREEN if letter == SECRET_WORD[i] else color
        text_surface = font.render(letter, True, color)
        screen.blit(text_surface, (i * (FONT_SIZE + MARGIN) + MARGIN, row * (FONT_SIZE + MARGIN) + MARGIN))

def display_message(message):
    text_surface = font.render(message, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(current_guess) == WORD_LENGTH and not game_won and not game_lost:
                    guesses.append(current_guess)
                    if current_guess == SECRET_WORD:
                        game_won = True
                    elif len(guesses) == MAX_ATTEMPTS:
                        game_lost = True
                    current_guess = ""
            elif event.key == pygame.K_BACKSPACE:
                current_guess = current_guess[:-1]
            elif event.unicode.isalpha() and len(current_guess) < WORD_LENGTH and not game_won and not game_lost:
                current_guess += event.unicode.upper()
    
    draw()

pygame.quit()
sys.exit()