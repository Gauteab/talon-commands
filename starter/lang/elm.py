from talon.voice import Context, Key
from ..utils import is_filetype
ctx = Context("elm", func=is_filetype(("elm",)))
ctx.keymap(
    {
        "import everything": ["import  exposing (..)"] + [Key("left")]*14,
        "case of": ["case  of"] + [Key("left")]*3,
        "new type": ["type  =" ] + [Key("left")]*2,
        "type alias": ["type alias  ="]+ [Key("left")]*2,
        "pizza right": " |> ",
        "pizza left": " <| ",

        "list map": "List.map ",
        "list filter": "List.filter ",
        "list fold": "List.foldr ",

        "P map": "P.map ",

        "default branch": "_ -> Debug.todo \"\"",
        "debug to do":[ "Debug.todo \"\"" ,Key("left")],
        "debug to string": "Debug.toString ",
        "debug log": "Debug.log \"\" ",

    }
)
