
import json
import os
from .enabler import is_enabled, ToggleContext
from talon.voice import Context, Key, Str
from .community_utils import is_filetype, insert, text, join_words
from talon import fs

context = ToggleContext("names", enabled=True)
# context.keymap({
#     "call {names.names}": lambda m: insert(f"{m[1]} "),
#     "{names.names} {names.names}": lambda m: insert(f"{m[0]} {m[1]} ")
# })


def load_names(path):
    with(open(path, 'r')) as f:
        obj = json.loads(f.read())
        print(obj)
        context.set_list("modules", obj["modules"])
        # lines = [s.rstrip() for s in f.readlines()]
        # context.set_list("names", lines)


def call_back(path, exists):
    if not exists:
        return
    print("\n\nchanged")
    load_names(path)


PATH = os.path.expanduser("~/.names")
load_names(PATH)
fs.watch(PATH, call_back)
