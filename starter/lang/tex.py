from talon.voice import Context, Key, Str, press
from ..utils import is_filetype

targets = ["text", "itemize", "tabular", "center", "minted"]
simple_commands = ["chapter", "part", "section", "subsection", "paragraph", "subparagraph", "item"]
text_commands = {"bold": "textbf", "italic": "textit"}

def begin(m):
    Str(f"\\begin{{{m[1]}}}\n\n\\end{{{m[1]}}}")(None)
    press("up")
    press("tab")

def command(s):
    Str(f"\\{s}{{}}")(None)
    press("left")


ctx = Context("latex", func=is_filetype(("tex",)))
ctx.keymap(
    {
        "use package": lambda m: command("usepackage"),
        "add {latex.simple}": lambda m: command(m[1]),
        "begin {latex.targets}": begin,
        "text {latex.text}": lambda m: command(text_commands[m[1]])

    }
)

ctx.set_list("targets", targets)
ctx.set_list("simple", simple_commands)
ctx.set_list("text", text_commands)

