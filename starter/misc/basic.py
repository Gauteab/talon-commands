from talon.voice import Context, Str, press, Key
from talon import ctrl

import string

alpha_alt = "air bat cap drum each far guest harp sit Jack Kate look made near out pit quench red sir trap urge verb who plex yank said".split()


f_keys = {f"F {i}": f"f{i}" for i in range(1, 13)}
# arrows are separated because 'up' has a high false positive rate
arrows = ["left", "right", "up", "down"]
simple_keys = ["tab", "escape", "enter", "space", "pageup", "pagedown"]
alternate_keys = {"delete": "backspace", "forward delete": "delete"}
symbols = {
    "back tick": "`",
    "comma": ",",
    "dot": ".",
    "period": ".",
    "semi": ";",
    "semicolon": ";",
    "tick": "'",
    "L square": "[",
    "left square": "[",
    "square": "[",
    "R square": "]",
    "right square": "]",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    "plus": "+",
    "dash": "-",
    "equals": "=",
}
modifiers = {
    "command": "cmd",
    "control": "ctrl",
    "shift": "shift",
    "alt": "alt",
    "option": "alt",
}

alphabet = dict(zip(alpha_alt, string.ascii_lowercase))
digits = {str(i): str(i) for i in range(10)}
simple_keys = {k: k for k in simple_keys}
arrows = {k: k for k in arrows}
keys = {}
keys.update(f_keys)
keys.update(simple_keys)
keys.update(alternate_keys)
keys.update(symbols)

# map alnum and keys separately so engine gives priority to letter/number repeats
keymap = keys.copy()
keymap.update(arrows)
keymap.update(alphabet)
keymap.update(digits)


def insert(s):
    Str(s)(None)


def get_modifiers(m):
    try:
        return [modifiers[mod] for mod in m["basic.modifiers"]]
    except KeyError:
        return []


def get_keys(m):
    groups = ["basic.keys", "basic.arrows", "basic.digits", "basic.alphabet"]
    for group in groups:
        try:
            return [keymap[k] for k in m[group]]
        except KeyError:
            pass
    return []


def uppercase_letters(m):
    insert("".join(get_keys(m)).upper())


def press_keys(m):
    mods = get_modifiers(m)
    keys = get_keys(m)
    if mods:
        press("-".join(mods + [keys[0]]))
        keys = keys[1:]
    for k in keys:
        press(k)


ctx = Context("basic")
ctx.keymap(
    {
        "(uppercase | ship) {basic.alphabet}+ [(lowercase | sunk)]": uppercase_letters,
        "{basic.modifiers}* {basic.alphabet}+": press_keys,
        "{basic.modifiers}* {basic.digits}+": press_keys,
        "{basic.modifiers}* {basic.keys}+": press_keys,
        "(go | {basic.modifiers}+) {basic.arrows}+": press_keys,
        "slap": [Key("enter")],
        "copy": [Key("cmd-c")],
        "paste": [Key("cmd-v")],
        "cut": [Key("cmd-x")],
        "spotlight": [Key("cmd-space")],
        "kick": lambda _: ctrl.mouse_click(button=0, hold=100),
        "next instance": Key("alt-cmd-minus"),
        "toolbar": Key("ctrl-f2"),
        "dredge": Key("cmd-tab"),
        "ross": Key("right"),
        "lease": Key("left"),
        "dunce": Key("down"),
        "sause": Key("up"),

    }
)
ctx.set_list("alphabet", alphabet.keys())
ctx.set_list("arrows", arrows.keys())
ctx.set_list("digits", digits.keys())
ctx.set_list("keys", keys.keys())
ctx.set_list("modifiers", modifiers.keys())

ctx.vocab = ["elm", "app", "parse"]
