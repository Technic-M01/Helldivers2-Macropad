"""
[3] [7] [11] [15] - layer 3
[2] [6] [10] [14] - layer 2
[1] [5] [9]  [13] - layer 1
[0] [4] [8]  [12] - layer 0
"""

from definitions import StratagemInputs, KeyColors

class Layers:
    def __init__(self, padKeys):
        self.keys = padKeys

        self.current_layer = 0

        self.selector_keys = {
            0: KeyColors.WHITE, #custom layer
            1: KeyColors.RED,   #offensive stratagems
            2: KeyColors.CYAN,  #support stratagems
            3: KeyColors.GREEN  #reinforcement stratagems
            }
        
        self.layer_keys = {
            5: KeyColors.OFF,
            6: KeyColors.OFF,
            7: KeyColors.OFF,
            9: KeyColors.OFF,
            10: KeyColors.OFF,
            11: KeyColors.OFF,
            13: KeyColors.OFF,
            14: KeyColors.OFF,
            15: KeyColors.OFF,
            }
        
        self.quick_action_keys = {
            4: KeyColors.YELLOW,
            8: KeyColors.ORANGE,
            12: KeyColors.PURPLE
            }
        
        layer_0 = {
            5:  None,
            9:  None,
            13: None,
            6:  None,
            10: None,
            14: None,
            7:  None,
            11: None,
            15: None 
            }

                # offensive stratagems
        layer_1 = {
            5:  StratagemInputs.orbital_laser,              #\
            9:  StratagemInputs.orbital_railcannon,         # |---- first row on macropad
            13: StratagemInputs.eagle_500kg,                #/
            6:  StratagemInputs.eagle_110mm_rocket_pods,    #\
            10: StratagemInputs.eagle_cluster_bomb,         # |---- second row on macropad
            14: StratagemInputs.eagle_napalm_airstrike,     #/
            7:  StratagemInputs.orbital_gas_strike,         #\
            11: StratagemInputs.orbital_percision_strike,   # |---- third row on macropad
            15: StratagemInputs.orbital_ems_strike          #/
            }

        # support stratagems
        layer_2 = {
            5:  StratagemInputs.autocannon, #\
            9:  StratagemInputs.recoilless_rifle, # |---- first row on macropad
            13: StratagemInputs.flamethrower, #/
            6:  StratagemInputs.spear, #\
            10: StratagemInputs.machine_gun, # |---- second row on macropad
            14: StratagemInputs.railgun, #/
            7:  StratagemInputs.guard_dog, #\
            11: StratagemInputs.grenade_launcher, # |---- third row on macropad
            15: StratagemInputs.patriot_exosuit  #/
            }
        layer_3 = {
            5:  StratagemInputs.mortar_sentry,
            9:  StratagemInputs.autocannon_sentry,
            13: StratagemInputs.rocket_sentry,
            6:  StratagemInputs.tesla_tower,
            10: StratagemInputs.shield_generator_relay,
            14: None,
            7:  None,
            11: None,
            15: None 
            }
        
        self.quick_action_layer = {
            4: StratagemInputs.reinforce,
            8: StratagemInputs.resupply,
            12: None
        }
        
        self.allLayers = [layer_0, layer_1, layer_2, layer_3]  
        self.setDefaultKeys()

    # sets up leds for selector and quick action keys
    def setDefaultKeys(self):
        for i in self.selector_keys:
            k = self.keys[i]
            k.rgb = self.selector_keys[i]
            k.led_on()
        for i in self.quick_action_keys:
            k = self.keys[i]
            k.rgb = self.quick_action_keys[i]
            k.led_on()
        
        self.checkLayerChange(1) #initialize with layer 0

    def checkLayerChange(self, keyNumber):
        if keyNumber in self.selector_keys.keys():
            self.current_layer = keyNumber
            layer_color = self.selector_keys[keyNumber]
            for i in self.layer_keys:
                k = self.keys[i]
                k.rgb = layer_color
                k.led_on()

    def getStratagem(self, keyNumber):
        layer = self.allLayers[self.current_layer]
        if keyNumber in layer.keys():
            return layer[keyNumber]
        elif keyNumber in self.quick_action_layer.keys():
            return self.quick_action_layer[keyNumber]
        else:
            return None

    def getSelectorKeys(self):
        return self.selector_keys
    
    def getLayerKeys(self):
        return self.layer_keys

    def getQuickActionKeys(self):
        return self.quick_action_keys
