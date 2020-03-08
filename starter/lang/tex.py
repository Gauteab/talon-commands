from talon.voice import Context, Key, Str, press
from ..utils import is_filetype

targets = ["text", "itemize"]
simple_commands = ["chapter", "part", "section", "subsection", "paragraph", "subparagraph", "item"]

def begin(m):
    Str(f"\\begin{{{m[1]}}}\n\n\\end{{{m[1]}}}")(None)
    press("up")

def command(m):
    Str(f"\\{m[1]}{{}}")(None)
    press("left")


ctx = Context("latex", func=is_filetype(("tex",)))
ctx.keymap(
    {
        "add {latex.simple}": command,
        "begin {latex.targets}": begin

    }
)

ctx.set_list("targets", targets)
ctx.set_list("simple", simple_commands)

