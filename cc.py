import pyautogui
import time
from pynput import mouse, keyboard

target_color = None
scanning = False

def on_click(x, y, button, pressed):
    if pressed:
        global target_color
        # Pobieramy kolor piksela w miejscu kliknięcia
        target_color = pyautogui.pixel(x, y)
        print(f"Color sampled: {target_color}")
        return False

def on_press(key):
    global scanning
    if key == keyboard.Key.space:
        scanning = not scanning
        print(f"Scanning: {scanning}")

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Click anywhere to sample color. Press SPACE to toggle scanning.")

# Czekanie na próbkowanie
with mouse.Listener(on_click=on_click) as m_listener:
    m_listener.join()

try:
    while True:
        if scanning:
            # ROBIMY ZRZUT EKRANU
            screenshot = pyautogui.screenshot()
            width, height = screenshot.size
            
            # Przeszukujemy ekran w poszukiwaniu koloru (co 10 pikseli dla szybkości)
            for x in range(0, width, 10):
                for y in range(0, height, 10):
                    if screenshot.getpixel((x, y)) == target_color:
                        print(f"Found color at {x}, {y}! Clicking...")
                        pyautogui.click(x, y)
                        time.sleep(1)
                        break 
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopped.")
