from talon.voice import Key, Context
from ... community_utils import is_not_vim
from ..utils import press

cli = Context("commandline", bundle="com.googlecode.iterm2", func=is_not_vim)
cli.keymap({
    "PB copy": "pbcopy",
    "exit session": [Key("ctrl-c"), "exit\n"],
    "clear session": [Key("ctrl-c"), "clear\n"],
    "clean": Key("cmd-k"),
    "rerun": [Key("up"), Key("enter")],
    "CD": "cd ",
    "CD up": ["cd ..", Key("enter")],
    "foreground": ['fg', Key('enter')],
    "edit": "vim ",
    "editor": ["vim", Key("enter")],
    "edit file": ["vim", Key("enter space g")],
    "brew install": "brew install ",
    "make dirk": "mkdir ",
    "remove dirk": "rm -rf ",
    "do move": "mv ",
    "open": "open ",
    "open charm": ["charm .", Key("enter")],
    "npm": "npm ",
    "R grep": "rg ",
    "user commands": ["cd ~/.talon/user/talon-commands", Key("enter")],
    "dash dash": " --",

    # Elm
    "helm repel": "elm repl",
    "helm install": "elm install ",
    "helm in it": "elm init ",
    "helm make": "elm make",
    "helm-app start": "elm-app start",
    "helm-app build": "elm-app build",
    "create helm app": "create-elm-app ",

    "list files": Key("l enter"),
    "find file": Key("ctrl-g"),
    "find (his | history)": Key("ctrl-r"),

    "conda": "conda ",
})


ctx = Context("iterm", bundle="com.googlecode.iterm2")
ctx.keymap({
    "new tab": Key("cmd-t"),
    "close tab": Key("cmd-w"),
    "next tab": Key("cmd-right"),
    "last tab": Key("cmd-left"),
    "preferences": Key("cmd-,"),
    "suspend": Key('ctrl-z'),
    "split horizontal": Key("cmd-shift-d"),
    "split vertical": Key("cmd-d"),
    "split {iterm.direction}": lambda m: press(f'cmd-alt-{m[1]}'),
})

ctx.set_list("direction", "left right up down".split())
