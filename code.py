
from kmk.kmk_keyboard import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
import board
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys


encoder_handler = EncoderHandler()
keyboard = KMKKeyboard()
# keyboard.modules.append(Layers())
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())

encoder_handler.pins = (
                         (board.GP0, board.GP20,board.GP2, False,3),
                        )
Zoom_in = KC.LCTRL(KC.EQUAL)
Zoom_out = KC.LCTRL(KC.MINUS)

encoder_handler.map = [ 
                        (( Zoom_in, Zoom_out,KC.C),( KC.D, KC.E,KC.F)),
                        (( KC.C, KC.C,KC.C),( KC.C, KC.C,KC.C))
]
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.tap_time = 250
keyboard.debug_enabled = True

# keyboard.col_pins = (
#     board.GP2, board.GP6, board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15,board.GP16,board.GP17,board.GP18,board.GP1,board.GP5,board.GP4,board.GP3
# )
# keyboard.row_pins = (board.GP19,board.GP21,board.GP22,board.GP26,board.GP27,board.GP28)

# keyboard.keymap = [ 
#     [
#         KC.NO,      KC.ESC,     KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12,     KC.NO,      KC.NO,      KC.NO,      KC.NO,   
		
# 		KC.GRV,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,      KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL,     KC.BSLS,    KC.BSPC,    KC.NO,      KC.NO,      KC.NO, 
# 		KC.TAB,     KC.NO,      KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.LBRC,    KC.RBRC,    KC.NO,      KC.NO,      KC.NO,      KC.NO, 
# 		KC.CAPS,    KC.NO,      KC.NO,      KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,    KC.ENT,     KC.NO,      KC.NO,      KC.NO,
# 		KC.LSFT,    KC.NO,      KC.NO,      KC.NO,      KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.LSFT,    KC.NO,      KC.UP,      KC.NO,         
#         KC.LCTL,    KC.NO,      KC.NO,      KC.NO,      KC.LGUI,    KC.LALT,    KC.NO,      KC.SPC,     KC.NO,      KC.NO,      KC.NO,      KC.LALT,    KC.LGUI,    KC.NO,      KC.LCTL,    KC.LEFT,    KC.DOWN,    KC.RIGHT
#     ]
#     ]

keyboard.col_pins = (board.GP18,) 
keyboard.row_pins = (board.GP16,)
keyboard.keymap = [ [KC.Z,],]


if __name__ == '__main__':
    keyboard.go()
