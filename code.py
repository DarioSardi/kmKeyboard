
from kmk.kmk_keyboard import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
import board as b

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.col_pins = (
    b.GP2, b.GP6, b.GP7,b.GP8,b.GP9,b.GP10,b.GP11,b.GP12,b.GP13,b.GP14,b.GP15,b.GP16,b.GP17,b.GP18,b.GP1,b.GP3,b.GP4,b.GP5
)
keyboard.row_pins = (b.GP19,b.GP21,b.GP22,b.GP26,b.GP27,b.GP28)

keyboard.keymap = [ 
    [
        KC.NO,      KC.ESC,     KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12,     KC.NO,      KC.NO,      KC.NO,      KC.NO,   
		
		KC.GRV,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,      KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL,     KC.BSLS,    KC.BSPC,    KC.NO,      KC.NO,      KC.NO, 
		KC.TAB,     KC.NO,      KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.LBRC,    KC.RBRC,    KC.ENT,     KC.NO,      KC.NO,      KC.NO, 
		KC.CAPS,    KC.NO,      KC.NO,      KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,    KC.NO,      KC.NO,      KC.NO,      KC.NO,
		KC.LSFT,    KC.NO,      KC.NO,      KC.NO,      KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.LSFT,    KC.NO,      KC.UP,      KC.NO,         
        KC.LCTL,    KC.NO,      KC.NO,      KC.NO,      KC.LGUI,    KC.LALT,    KC.NO,      KC.SPC,     KC.NO,      KC.NO,      KC.NO,      KC.LALT,    KC.LGUI,    KC.NO,      KC.LCTL,    KC.LEFT,    KC.DOWN,    KC.RIGHT
    ]
    ]

if __name__ == '__main__':
    keyboard.go()
