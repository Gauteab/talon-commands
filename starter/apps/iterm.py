from talon.voice import Key, Context

ctx = Context("iterm", bundle="com.googlecode.iterm2")

keymap = {
    "preferences": Key("cmd-,"),
    "exit session": [Key("ctrl-c"), "exit\n"],
    "clear session": [Key("ctrl-c"), "clear\n"],
    "clean": Key("cmd-k"),
    "rerun": [Key("up"), Key("enter")],
    "CD": "cd ",
    "CD up": ["cd ..", Key("enter")],
    "foreground": ['fg', Key('enter')],
    "suspend": Key('ctrl-z'),
    "edit": "vim ",
    "brew install": "brew install ",
    "make directory": "mkdir ",
    "split horizontal": Key("cmd-shift-d"),
    "split vertical": Key("cmd-d"),
}

keymap.update({f"split {direction}": Key(f"cmd-alt-{direction}") for direction in "left right up down".split()})

ctx.keymap(keymap)
