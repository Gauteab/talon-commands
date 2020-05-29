from talon.voice import Key, Context
from .. utils import is_in_bundles
from ... bundle_groups import EDITOR_BUNDLES

ctx = Context("idea", func=is_in_bundles(EDITOR_BUNDLES))

keymap = {
    "search for": Key("cmd-alt-s"),
    "scroll down": Key("cmd-alt-down"),
    "scroll up": Key("cmd-alt-up"),
    "find action": Key("cmd-alt-ctrl-a"),
    "definition": Key("alt-space"),
    "rename": Key("shift-f6"),
    "next error": Key("f2"),
    "last error": Key("shift-f2"),
    "suggest": Key("alt-enter"),
    "next tab": Key("cmd-shift-["),
    "go to": Key("cmd-ctrl-g"),

    "next cell": Key("ctrl-j"),
    "last cell": Key("ctrl-k"),
    "run cell": Key("ctrl-enter"),
    "run all": Key("ctrl-alt-shift-enter"),
    "jupiter stop": Key("cmd-alt-ctrl-s"),
    "jupiter console": Key("ctrl-alt-j"),
}

ctx.keymap(keymap)
