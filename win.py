import pygame
import tkinter as tk
import sys
import subprocess
from const import *


def start_game():
    # Закрываем текущее окно
    root.destroy()
    # Запуск файла game.py
    subprocess.run([sys.executable, "game.py"])

def exit_game():
    pygame.quit()
    root.destroy()
    sys.exit()


def main():
    global root
    root = tk.Tk()
    root.title("My Game")
    
    # Создаем фрейм для вступленияc
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True)
    
    title = tk.Label(frame, text="WIN!!", font=("Helvetica", 16, "bold"))
    title.pack(pady=10)
    
    # Создаем стили для кнопок
    button_style = {
        "font": ("Helvetica", 14),
        "bg": "white",
        "fg": "blue",
        "relief": tk.RAISED,
        "bd": 2,
        "highlightbackground": "blue",
        "highlightthickness": 2,
        "activebackground": "lightblue",
        "activeforeground": "blue",
        "width": 20,
        "height": 2
    }
    
    exit_button = tk.Button(frame, text="Exit", command=exit_game, **button_style)
    exit_button.pack(side=tk.RIGHT, padx=10, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()

