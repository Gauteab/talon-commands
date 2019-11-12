from talon.voice import Context, Key

context = Context("GoogleChrome", bundle="com.google.Chrome")

keymap = {
    "address bar": Key("cmd-l"),
    "go back": Key("cmd-["),
    "go forward": Key("cmd-]"),
    "chrome (find | marco)": Key("cmd-f"),
    "dev tools": Key("cmd-alt-i"),
    # navigating current page
    "scroll top": Key("g g"),
    "scroll (bottom | end)": Key("G"),
    "[open] link": Key("f"),
    "[open] link new": Key("F"),
    "copy (address | url)": Key("escape y y"),
    "(refresh | reload)": Key("cmd-r"),
    "view source": Key("g s"),
    "insert mode": Key("i"),
    "next frame": Key("g f"),
    "main frame": Key("g F"),
    # navigating to new pages
    "(open | go) (url | history)": Key("o"),
    "(open | go) (url | history) new": Key("O"),
    "(open | go) bookmark": Key("b"),
    "(open | go) bookmark new": Key("B"),
    # manipulating tabs
    "restore tab": Key("X"),
    "search tabs": Key("T"),
    "close tab": Key("cmd-w"),
    "new tab": Key("cmd-t"),
    "next tab": Key("ctrl-tab"),
    "prior tab": Key("shift-ctrl-tab"),
}

context.keymap(keymap)
