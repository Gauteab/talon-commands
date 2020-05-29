
from talon.voice import Context, Key
from ..utils import is_filetype

ctx = Context("ML", func=is_filetype(("hs", "elm")))
ctx.keymap(
    {
        "value true": " True ",
        "value false": " False ",
        "import": "import ",
        "case of": ["case  of"] + [Key("left")]*3,
        "if else": ["if  then 0 else 1"] + [Key("left")]*14,
        "lamda": ["(\\x -> )"]+ [Key("left")],
        "type list": "List",
        "type map": "Map",
        "type boolean": "Bool",
        "type string": "String",
        "type either": "Either",
        "type char": "Char",
        "type set": "Set",
        "type integer": "Int",
    }
)
