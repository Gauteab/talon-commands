from talon.voice import Context, Key
from ..utils import is_filetype

ctx = Context("haskell", func=is_filetype(("hs",)))
ctx.keymap(
    {
        "of type": " :: ",
        "import": "import ",
        "import qualified": "import qualified ",
        "deriving": " deriving ",
        "case of": ["case  of"] + [Key("left")]*3,
        "new type": ["type  =" ] + [Key("left")]*2,
        "data type": ["data  =" ] + [Key("left")]*2,
        "type alias": ["type alias  ="]+ [Key("left")]*2,
        "lamda": ["(\\x -> )"]+ [Key("left")],
        "pizza left": " $ ",
        "pizza right": " & ",
        "type list": "List",
        "type map": "Map",
        "type boolean": "Bool",
        "type string": "String",
        "type either": "Either",
        "type char": "Char",
        "type set": "Set",
        "type integer": "Int",
        "F map": "fmap ",
        "list map": "map ",
        "list filter": "filter ",
        "list fold": "foldr ",

    }
)
