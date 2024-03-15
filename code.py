from pmk import PMK
from pmk.platform.keybow2040 import Keybow2040 as Hardware          # for Keybow 2040
# from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware  # for Pico RGB Keypad Base

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from definitions import StratagemInputs

import LayerConfig

import time

pmk = PMK(Hardware())
keys = pmk.keys

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

keymap = [Keycode.ZERO,
         Keycode.ONE,
         Keycode.TWO,
         Keycode.THREE,
         Keycode.FOUR,
         Keycode.FIVE,
         Keycode.SIX,
         Keycode.SEVEN,
         Keycode.EIGHT,
         Keycode.NINE,
         Keycode.A,
         Keycode.B,
         Keycode.C,
         Keycode.D,
         Keycode.E,
         Keycode.F]

eagle500 = StratagemInputs.eagle_500kg


layers = LayerConfig.Layers(keys)

selectorKeys = layers.getSelectorKeys()
layerKeys = layers.getLayerKeys()

# sends keyboard inputs to call the provided stratagem
def callStratagem(stratagem):
    if stratagem is None:
        print("error getting stratagem")
    else:
        for key in stratagem:
            keyboard.send(key)
            time.sleep(0.1) # to avoid race conditions

#sets up handler for key presses
for key in keys:
    @pmk.on_press(key)
    def press_handler(key):
        keycode = keymap[key.number]
        print("key pressed: ", keycode)
        print("key number: ", key.number)


        if key.number in selectorKeys.keys():
            layers.checkLayerChange(key.number)

        elif key.number in layerKeys.keys():
            strat = layers.getStratagem(key.number)
            callStratagem(strat)


while True:
    pmk.update()
