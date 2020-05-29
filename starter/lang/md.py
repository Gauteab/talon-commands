
from talon.voice import Context, Key, Str, press
from ..utils import is_filetype


ctx = Context("md", func=is_filetype(("md",)))
ctx.keymap(
    {
        "math times": " \\cdot ",
        "left arrow": " \\leftarrow ",
        "math mode": ["$$", Key("left")]

    }
)


