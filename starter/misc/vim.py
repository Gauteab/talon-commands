from talon.voice import Context, Key
import time
from ... bundle_groups import EDITOR_BUNDLES
from .. utils import is_in_bundles

context = Context("vim")
Normal = Key("ctrl-c")
context.keymap(
    {
        "norm": Normal,
        "suspend": Key("ctrl-z"),
        # "go to": [Normal, Key("enter")],

        # Editing
        "insert end": [Normal, "A"],
        "insert start": [Normal, "I"],
        "insert over": [Normal, "O"],
        "insert under": [Normal, "o"],
        "duplicate line": [Normal, "yyp"],

        "complete": Key("ctrl-n"),

        # File management
        "save it": [Normal, ":w", Key("enter")],
        "quit it": [Normal, ":q", Key("enter")],
        "quit hard": [Normal, ":q!", Key("enter")],
        "save and quit": [Normal, ":wq", Key("enter")],

        # Navigation
        "jump down": [Normal, Key("ctrl-d")],
        "jump up": [Normal, Key("ctrl-u")],
        "forward": [Normal, "f"],
        "backward": [Normal, "F"],
        "toward": [Normal, "t"],
        "back toward": [Normal, "T"],
        "next block": [Normal, "}"],
        "last block": [Normal, "{"],
        "scroll bottom": [Normal, "G"],
        "scroll top": [Normal, "gg"],
        "middle screen": [Normal, "M"],
        "scan": [Normal, "/"],
        "scan back": [Normal, "?"],

        "undo": [Normal, "u"],
        "redo": [Normal, Key("ctrl-r")],

        "change word": [Normal, "ciw"],
        "change line": [Normal, "cc"],
        "change forward": [Normal, "C"],
        "change string": [Normal, "ci\""],
        "change paragraph": [Normal, "cip"],

        "delete word": [Normal, "diw"],
        "delete line": [Normal, "dd"],
        "delete forward": [Normal, "D"],
        "delete paragraph": [Normal, "dip"],

        "visual mode": [Normal, "v"],
        "visual line": [Normal, "V"],

        "comment line": [Normal, "gcc"],
        "comment (paragraph | par)": [Normal, "gcip"],

        "run it": Key("ctrl-c f9"),
        "align table": [Normal, "gaip*|"]
    }
)
