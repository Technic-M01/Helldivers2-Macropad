from adafruit_hid.keycode import Keycode

class KeyColors:
    """
    RBG values for common colors
    """

    PURPLE = (255, 0, 100) # default purple
    YELLOW = (255, 255, 0)
    ORANGE = (252, 73, 3)
    RED = (255, 0, 0)
    CYAN = (0, 255, 255)
    GREEN = (0, 255, 25) # modifier key green
    OFF = (0, 0, 0)
    WHITE = (255, 255, 255)
"""
RIGHT_ARROW = 0x4F  Move the cursor right
LEFT_ARROW = 0x50   Move the cursor left
DOWN_ARROW = 0x51   Move the cursor down
UP_ARROW = 0x52     Move the cursor up
"""

class StratagemInputs:
    #Admin Center Strategems
    machine_gun =               [Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW]

    anti_material_rifle =       [Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.DOWN_ARROW]

    stalwart =                  [Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW]

    expendable_anti_tank =      [Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW]

    recoilless_rifle =          [Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.LEFT_ARROW]

    flamethrower =              [Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW]

    autocannon =                [Keycode.DOWN_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW]

    railgun =                   [Keycode.DOWN_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.RIGHT_ARROW]

    spear =                     [Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW]

    #Orbital Cannons Strategems
    """
    MISSING:
    - orbital 120mm barrage
    - orbital walking barrage
    """
    orbital_gatling =           [Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.UP_ARROW]

    orbital_airburst =          [Keycode.RIGHT_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.RIGHT_ARROW]

    orbital_380_barrage =       [Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW]

    orbital_laser =             [Keycode.RIGHT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.LEFT_ARROW]

    orbital_railcannon =        [Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW]


    #Hanger Strategems
    eagle_strafing_run =        [Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.RIGHT_ARROW]

    eagle_airstrike =           [Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.RIGHT_ARROW]

    eagle_cluster_bomb =        [Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW]

    eagle_napalm_airstrike =    [Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW]

    jump_pack =                 [Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW]

    eagle_smoke_strike =        [Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.DOWN_ARROW]

    eagle_110mm_rocket_pods =   [Keycode.UP_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW]

    eagle_500kg =               [Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW]

    #Bridge Strategems
    """
    MISSING:
    - orbital smoke strike
    - HMG emplacement
    """
    orbital_percision_strike =  [Keycode.RIGHT_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.UP_ARROW]

    orbital_gas_strike =        [Keycode.RIGHT_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.RIGHT_ARROW]

    orbital_ems_strike =        [Keycode.RIGHT_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW]

    shield_generator_relay =    [Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW]

    tesla_tower =               [Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.RIGHT_ARROW]

    #Engineering Bay Strategems
    """
    MISSING:
    - anti-personnel minefield
    - laser cannon
    - incendiary mines
    - ballistic shield backpack
    - arc thrower
    """
    supply_pack =               [Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.DOWN_ARROW]

    grenade_launcher =          [Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW]

    guard_dog_rover =           [Keycode.DOWN_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW]

    shield_generator_pack =     [Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.RIGHT_ARROW]

    #Robotics Workshop Strategems
    """
    MISSING:
    - machine gun sentry
    - gatling sentry
    """
    mortar_sentry =             [Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW]

    guard_dog =                 [Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.DOWN_ARROW]

    autocannon_sentry =         [Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.UP_ARROW]

    rocket_sentry =             [Keycode.DOWN_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.LEFT_ARROW]

    patriot_exosuit =           [Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.UP_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.DOWN_ARROW]

    #Mission Specific Strategems
    """
    MISSING:
    - super earth flag
    - resupply
    - upload data
    - hell bomb
    """
    reinforce =                 [Keycode.UP_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.LEFT_ARROW,
                                Keycode.UP_ARROW]

    sos_beacon =                [Keycode.UP_ARROW,
                                Keycode.DOWN_ARROW,
                                Keycode.RIGHT_ARROW,
                                Keycode.UP_ARROW]


class ConfigCodes:
    """
    ad-hoc enum class to hold labels for the keys of the keybow config dictionary
    """

    KEYS = "keys"                                    # keys on the Keybow2040
    SELECTORS = "selector_keys"                      # keys that can act as selector keys
    DEDICATED_SELECTORS = "dedicated_selector_keys"  # keys that ONLY act as selector keys
    LAYER_COLORS = "layer_colors"                    # list of colors associated with each layer
    LAYERS = "layers"                                # layers of functionality on the macro pad

# dict(s) of Keycodes mapped to the value of the keys they represent.
#  they Keycodes are hexadecimal, so the key(s) of the dict(s) below are the int value of the hex
KEY_CODE_MAP = {
    39: 0,
    30: 1,
    31: 2,
    32: 3,
    33: 4,
    34: 5,
    35: 6,
    36: 7,
    37: 8,
    38: 9,
    40: "ENTER",
    42: "BACKSPACE"
}

CONSUMER_CONTROL_CODE_MAP = {
    111: "BRIGHTNESS_INCREMENT",
    112: "BRIGHTNESS_DECREMENT",
    181: "SCAN_NEXT_TRACK",
    182: "SCAN_PREVIOUS_TRACK",
    233: "VOLUME_INCREMENT",
    234: "VOLUME_DECREMENT",
    205: "PLAY_PAUSE",
    226: "MUTE"
}

KEY_MAPPING = [
    [3, 7, 11, 15],
    [2, 6, 10, 14],
    [1, 5, 9, 13],
    [0, 4, 8, 12]
]
