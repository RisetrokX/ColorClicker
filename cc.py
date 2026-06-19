import pyautogui
from pynput import mouse, keyboard
import time

target_color = None
scanning = False

# Funkcja pobierająca kolor po kliknięciu myszą
def on_click(x, y, button, pressed):
    if pressed:
        global target_color
        target_color = pyautogui.pixel(x, y)
        print(f"Color sampled: {target_color}")
        return False # Zatrzymuje listener po jednym kliknięciu

# Funkcja sterująca skanowaniem
def on_press(key):
    global scanning
    if key == keyboard.Key.space: # Używamy spacji zamiast 'r'
        scanning = not scanning
        print(f"Scanning: {scanning}")

# Uruchamiamy listener klawiatury
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Click anywhere to sample color. Press SPACE to toggle scanning.")

try:
    while True:
        if scanning and target_color:
            # Szukanie koloru na ekranie
            location = pyautogui.locateOnScreen(target_color, confidence=0.9)
            if location:
                pyautogui.click(location)
                print("Clicked target!")
        
        # Czekanie na próbkowanie koloru
        if not target_color:
            with mouse.Listener(on_click=on_click) as m_listener:
                m_listener.join()
        
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopped.")
