from talon.voice import Context, Key

context = Context("symbols")

context.keymap(
    {
        "colon": ":",
        "question [mark]": "?",
        "tilde": "~",
        "(bang | exclamation point)": "!",
        "dollar [sign]": "$",
        "(downscore | underscore)": "_",
        "(paren | left paren)": "(",
        "(rparen | are paren | right paren)": ")",
        "(bracket | brack | left bracket)": "{",
        "(rbrack | are bracket | right bracket)": "}",
        "(angle | left angle | less than)": "<",
        "(rangle | are angle | right angle | greater than)": ">",
        "(star | asterisk)": "*",
        "(pound | hash [sign])": "#",
        "percent [sign]": "%",
        "caret": "^",
        "at sign": "@",
        "(and sign | ampersand )": "&",
        "pipe": "|",
        "(dubquote | double quote)": '"',
    }
)
