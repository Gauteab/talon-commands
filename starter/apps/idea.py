from talon.voice import Key, Context

ctx = Context("idea")#bundle="com.jetbrains.intellij")

keymap = {
    "search for": Key("cmd-alt-s"),
    "find action": Key("cmd-alt-ctrl-a"),
    "definition": Key("alt-space"),
    "rename": Key("shift-f6"),
    "next error": Key("f2"),
    "prior error": Key("shift-f2"),
    "suggest": Key("alt-enter"),
    "next tab": Key("cmd-shift-["),
    "go to": Key("cmd-ctrl-g"),

    "next cell": Key("ctrl-j"),
    "last cell": Key("ctrl-k"),
    "run cell": Key("ctrl-enter"),
    "run all": Key("ctrl-alt-shift-enter"),
    "jupiter console": Key("ctrl-alt-j"),
}

ctx.keymap(keymap)
