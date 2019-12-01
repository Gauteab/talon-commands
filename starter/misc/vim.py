from talon.voice import Context, Key
import time

context = Context("vim")
Normal = Key("left right escape")
context.keymap(
    {
        "insert end": [Normal, "A"],
        "insert start": [Normal, "I"],
        "insert over": [Normal, "O"],
        "insert under": [Normal, "o"],

        "dedent": [Normal, "<"],
        "indent": [Normal, ">"],

        "complete": Key("ctrl-n"),

        "save it": [Normal, ":w", Key("enter")],
        "quit it": [Normal, ":q", Key("enter")],
        "quit hard": [Normal, ":q!", Key("enter")],
        "save and quit": [Normal, ":wq", Key("enter")],


        "forward": [Normal, "f"],
        "backward": [Normal, "F"],
        "toward": [Normal, "t"],
        "back toward": [Normal, "T"],

        "duplicate line": [Normal, "yyp"],
        "scroll bottom": [Normal, "G"],
        "scroll top": [Normal, "gg"],
        "middle screen": [Normal, "M"],


        "undo": [Normal, "u"],
        "redo": [Normal, Key("ctrl-r")],
        "scan": [Normal, "/"],
        "scan back": [Normal, "?"],

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
    }
)
