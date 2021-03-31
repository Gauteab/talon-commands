
from talon.voice import Context, Key
from talon import voice, app

enabled = {}

class ToggleContext(Context):
    def __init__(self, name, enabled=False, alternative=None, func=None, **kwargs):
        key = alternative if alternative else name
        declare(key, enabled)
        func = is_enabled(key) if not func else is_enabled_or(key, func)
        super().__init__(name, func=func, **kwargs)

def is_enabled_or(name, f):
    return lambda a,w: enabled[name] or f(a,w)

def is_enabled(name):
    return lambda a,w: enabled[name]

def disable(m):
    app.notify(f'{m[1]} disabled')
    enabled[m[1]] = False

def enable(m):
    app.notify(body=f'{m[1]} enabled')
    enabled[m[1]] = True

context = Context("enabler")
context.keymap({
    "enable {enabler.enabled}": enable,
    "disable {enabler.enabled}": disable
})

def declare(name, value=False):
    enabled[name] = value
    context.set_list("enabled", enabled)

