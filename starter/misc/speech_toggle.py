from talon.voice import Context, ContextGroup, Key
from talon.engine import engine
from talon_plugins import speech

sleep_group = ContextGroup("sleepy")
sleepy = Context("sleepy", group=sleep_group)

sleepy.keymap(
    {
        "next slide": [Key("right")],
        "last slide": [Key("left")],
        "talon sleep": lambda m: speech.set_enabled(False),
        "talon wake": lambda m: speech.set_enabled(True),
        "dragon mode": [
            lambda m: speech.set_enabled(False),
            lambda m: engine.mimic("wake up".split()),
        ],
        "talon mode": [
            lambda m: speech.set_enabled(True),
            lambda m: engine.mimic("go to sleep".split()),
        ],
    }
)
sleep_group.load()
