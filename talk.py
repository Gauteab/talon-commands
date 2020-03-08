from talon import applescript
from talon.engine import engine
from talon.voice import Context, Key
from time import sleep

def friendly_message(m):
    sleep(0.5)
    applescript.run(r'''say "I love you too, friend." using "Alex" speaking rate 180 pitch 42 modulation 60''')

def oh_stop_it(m):
    sleep(0.5)
    applescript.run(r'''say "no, you stop it." using "Alex" speaking rate 180 pitch 42 modulation 60''')

context = Context("talk")
context.keymap({
    "i love my computer": friendly_message,
    "oh stop it you": oh_stop_it,
})
