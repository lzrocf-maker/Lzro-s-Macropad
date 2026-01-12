import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

# 1. Configuración de los Switches (Direct Pins según tu KiCad)
# Mapeados de SW1 a SW10
PINS = [
    board.D26, board.D27, board.D28, board.D29, board.D6,
    board.D7,  board.D0,  board.D1,  board.D2,  board.D3
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
    pull=True,
)

# 2. Configuración de los 16 LEDs RGB (Pin D4 / GPIO4)
rgb = RGB(pixel_pin=board.D4, num_pixels=16)
keyboard.extensions.append(rgb)

# 3. Mapa de teclas (Cámbialas a tu gusto)
keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,
        KC.N6, KC.N7, KC.N8, KC.N9, KC.N0,
    ]
]

if __name__ == '__main__':
    keyboard.go()