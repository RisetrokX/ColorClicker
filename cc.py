import pyautogui
import keyboard # pip install keyboard

# Słownik z podstawowymi kolorami (RGB)
COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

def get_color_at_mouse():
    x, y = pyautogui.position()
    return pyautogui.pixel(x, y)

def scan_and_click(target_color):
    print(f"Scanning for {target_color}...")
    # Przeszukuje ekran (screenshot jest najszybszą metodą dla całego ekranu)
    screen = pyautogui.screenshot()
    width, height = screen.size
    
    for x in range(0, width, 5): # Co 5 pikseli dla szybkości
        for y in range(0, height, 5):
            if screen.getpixel((x, y)) == target_color:
                pyautogui.click(x, y)
                return True
    return False

# Główna pętla
print("Press 's' to sample color from mouse position, 'r' to run, 'q' to quit.")
target = (0, 0, 0)

while True:
    if keyboard.is_pressed('s'):
        target = get_color_at_mouse()
        print(f"Target color sampled: {target}")
    
    if keyboard.is_pressed('r'):
        if scan_and_click(target):
            print("Clicked!")
            
    if keyboard.is_pressed('q'):
        break
