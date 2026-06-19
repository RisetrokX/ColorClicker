import pyautogui
from pynput import mouse
import time

# Zmienne globalne
target_color = None
scanning = False

# Funkcja pobierająca kolor po kliknięciu myszą
def on_click(x, y, button, pressed):
    if pressed:
        global target_color
        # Na Windowsie pyautogui.pixel działa natywnie
        target_color = pyautogui.pixel(x, y)
        print(f"Color sampled: {target_color} at ({x}, {y})")
        return False # Zatrzymuje nasłuchiwanie po jednym kliknięciu

print("--- Color Clicker for Windows ---")
print("1. Click anywhere to sample the target color.")
print("2. Once sampled, the script will start scanning.")

# 1. Próbkowanie koloru
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# 2. Skanowanie ekranu
print("Scanning started! Press Ctrl+C in terminal to stop.")
try:
    while True:
        # Pobieramy zrzut ekranu (Windows robi to błyskawicznie)
        screen = pyautogui.screenshot()
        width, height = screen.size
        
        # Skanowanie co 10 pikseli dla wydajności (zwiększ krok, jeśli tnie)
        for x in range(0, width, 10):
            for y in range(0, height, 10):
                if screen.getpixel((x, y)) == target_color:
                    print(f"Found color at {x}, {y}! Clicking...")
                    pyautogui.click(x, y)
                    time.sleep(1) # Czekaj chwilę po kliknięciu
        
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopped.")
