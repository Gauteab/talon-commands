from talon.voice import Context, Key
from ..utils import is_filetype
ctx = Context("elm", func=is_filetype(("elm",)))
ctx.keymap(
    {
        "case of": ["case  of"] + [Key("left")]*3,
        "new type": ["type  =" ] + [Key("left")]*2,
        "type alias": ["type alias  ="]+ [Key("left")]*2,
        "pizza right": " |> ",
        "pizza left": " <| ",
        "list": "List",
        "list map": "List.map ",
        "list filter": "List.filter ",
        "list fold": "List.foldr ",
    }
)
