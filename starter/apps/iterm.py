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
    "make dirk": "mkdir ",
    "do move": "mv ",
    "split horizontal": Key("cmd-shift-d"),
    "split vertical": Key("cmd-d"),

    "open": "open ",
    "npm": "npm ",
    "R grep": "rg ",
    "user commands": ["cd ~/.talon/user/talon-commands", Key("enter")],
    "dotfiles": ["cd ~/dotfiles", Key("enter")],

    "elm repel": "elm repl",
    "elm install": "elm install ",
    "elm make": "elm make",
    "elm-app start": "elm-app start",
    "elm-app build": "elm-app build",
    "create-elm-app": "create-elm-app ",

    "conda": "conda ",
}

keymap.update({f"split {direction}": Key(f"cmd-alt-{direction}") for direction in "left right up down".split()})

ctx.keymap(keymap)
ctx.vocab = ["elm"]
