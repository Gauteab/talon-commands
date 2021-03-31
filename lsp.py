# import json
# from itertools import groupby
# import os
# from .enabler import is_enabled, ToggleContext
# from talon.voice import Context, Key, Str
# from .community_utils import is_filetype, insert, text, join_words
# from talon import fs

# context = ToggleContext("lsp", enabled=True)
# dictionary = {}

# def load_names(path):
#     with(open(path, 'r')) as f:
#         obj = json.loads(f.read())
#         obj = sorted([(v["kind"],v["text"]) for v in obj])
#         dictionary = {key:list(v[1] for v in values) for key,values in groupby(obj, key=lambda x:x[0])}
#         for kind, values in dictionary.items():
#             context.set_list(kind, (values))
#             print(kind, values)

# def call_back(path, exists):
#     if not exists:
#         return
#     print("\n\nchanged")
#     load_names(path)


# PATH = os.path.expanduser("~/output.json")
# load_names(PATH)
# fs.watch(PATH, call_back)
