import re
from talon.voice import Context, Key, press

from ..community_utils import is_filetype, snake_text, insert
from .. import community_utils
from ..enabler import ToggleContext


FILETYPES = (".py", "ipynb")

ctx = Context("global_python")
exception_list = [
    "BaseException",
    "SystemExit",
    "KeyboardInterrupt",
    "GeneratorExit",
    "Exception",
    "StopIteration",
    "StopAsyncIteration",
    "ArithmeticError",
    "FloatingPointError",
    "OverflowError",
    "ZeroDivisionError",
    "AssertionError",
    "AttributeError",
    "BufferError",
    "EOFError",
    "ImportError",
    "ModuleNotFoundError",
    "LookupError",
    "IndexError",
    "KeyError",
    "MemoryError",
    "NameError",
    "UnboundLocalError",
    "OSError",
    "BlockingIOError",
    "ChildProcessError",
    "ConnectionError",
    "BrokenPipeError",
    "ConnectionAbortedError",
    "ConnectionRefusedError",
    "ConnectionResetError",
    "FileExistsError",
    "FileNotFoundError",
    "InterruptedError",
    "IsADirectoryError",
    "NotADirectoryError",
    "PermissionError",
    "ProcessLookupError",
    "TimeoutError",
    "ReferenceError",
    "RuntimeError",
    "NotImplementedError",
    "RecursionError",
    "SyntaxError",
    "IndentationError",
    "TabError",
    "SystemError",
    "TypeError",
    "ValueError",
    "UnicodeError",
    "UnicodeDecodeError",
    "UnicodeEncodeError",
    "UnicodeTranslateError",
    "Warning",
    "DeprecationWarning",
    "PendingDeprecationWarning",
    "RuntimeWarning",
    "SyntaxWarning",
    "UserWarning",
    "FutureWarning",
    "ImportWarning",
    "UnicodeWarning",
    "BytesWarning",
    "ResourceWarning",
]
exceptions = {
    " ".join(re.findall("[A-Z][^A-Z]*", exception)): exception
    for exception in exception_list
}


def raise_exception(m):
    insert(f"raise {exceptions[m['global_python.exception'][0]]}()")
    press("left")


def modify_selected_text(fn):
    def wrapper(m):
        utils.paste_text(fn(m, utils.copy_selected("")))

    return wrapper


def wrap_call(m):
    text = f"({utils.copy_selected('')})"
    utils.paste_text(text)
    for _ in range(len(text)):
        press("left")

    utils.snake_text(m)


def f_string(m):
    utils.paste_text('f"{' + utils.copy_selected("") + '}"')
    press("left")
    press("left")


ctx.keymap(
    {
        "dunder in it": "__init__",
        "dot pie": ".py",
        "dot pipe": ".py",
        "star (arguments | args)": "*args",
        "star star K wargs": "**kwargs",
        "raise {global_python.exception}": raise_exception,
    }
)
ctx.set_list("exception", exceptions.keys())

PREFIX = "(py | python)"
# ctx = Context("python")
ctx = ToggleContext("python", func=is_filetype(FILETYPES))
ctx.keymap(
    {
        "self assign <dgndictation> [over]": [
            "self.",
            snake_text,
            " = ",
            snake_text,
            "\n",
        ],
        "self": "self",
        "self dot": "self.",
        "self [(dot | doubt)] <dgndictation> [over]": ["self.", snake_text],
        "self [(dot | doubt)] private <dgndictation> [over]": ["self._", snake_text],
        # this isn't easy to write because snake_text always assumes it is
        # working on the first <dgndictation>, but this command has two of
        # them
        # "from <dgndictation> import [<dgndictation>] [over]": from_import ,
        "is not": " is not ",
        "F string": f_string,
        "wrap call [<dgndictation>]": wrap_call,
        f"{PREFIX} pass": "pass",
        f"{PREFIX} true": "True",
        f"{PREFIX} false": "False",
        f"{PREFIX} none": "None",
        f"{PREFIX} is": " is ",
        f"{PREFIX} as": " as ",
        f"{PREFIX} lambda": ["lambda "],
        f"{PREFIX} for": [" for "],
        f"{PREFIX} guard": [" if "],
        f"{PREFIX} in [<dgndictation>]": [" in ", snake_text],
        f"{PREFIX} if [<dgndictation>]": ["if :", Key("left"), snake_text],
        f"{PREFIX} else": "else:\n",
        f"{PREFIX} elif": ["elif :", Key("left")],
        f"{PREFIX} with": ["with :", Key("left")],
        f"{PREFIX} try": ["try", Key("tab")],
        f"{PREFIX} import [<dgndictation>] [over]": ["import ", snake_text],
        f"{PREFIX} from [<dgndictation>] [over]": ["from ", snake_text],
        f"{PREFIX} from [<dgndictation>] import": ["from ", snake_text, " import "],
        f"{PREFIX} length": ["len()", Key("left")],
        f"{PREFIX} class": "class ",
        f"{PREFIX} assert": "assert ",
        "call {lsp.Function}": [lambda m: insert(f"{m[1]}()"), Key("left")],
        # "{names.names} {names.names}": lambda m: insert(f"{m[0]}({m[1]})"),
        # "call <dgndictation> [over]": [snake_text, "()", Key("left")],
        f"define <dgndictation> [over]": ["def ", snake_text, "():", Key("left left")],
        f"define": ["def ():", Key("left " * 3)],
        "return [<dgndictation>] [over]": ["return ", snake_text],
        "while loop": ["while :", Key("left")],
        "for loop": ["for :", Key("left")],
    }
)
