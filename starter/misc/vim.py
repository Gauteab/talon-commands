from talon.voice import Context, Key

context = Context("vim")

context.keymap(
    {
        "insert end": [Key("escape"), "A"],
        "insert start": [Key("escape"), "I"],
        "insert over": [Key("escape"), "O"],
        "insert under": [Key("escape"), "o"],

        "save it": [Key("escape"), ":w", Key("enter")],
        "quit it": [Key("escape"), ":q", Key("enter")],
        "save and quit": [Key("escape"), ":wq", Key("enter")],
        "undo": [Key("escape"), "u"],
        "redo": [Key("escape"), Key("ctrl-r")],
        "scan": [Key("escape"), "/"],
        "scan back": [Key("escape"), "?"],

        "change word": [Key("escape"), "ciw"],
        "change line": [Key("escape"), "cc"],
        "change forward": [Key("escape"), "C"],
        "change string": [Key("escape"), "ci\""],
        "change paragraph": [Key("escape"), "cip"],

        "delete word": [Key("escape"), "diw"],
        "delete line": [Key("escape"), "dd"],
        "delete forward": [Key("escape"), "D"],
        "delete paragraph": [Key("escape"), "dip"],

        "visual mode": [Key("escape"), "v"],
        "visual line": [Key("escape"), "V"],
    }
)
