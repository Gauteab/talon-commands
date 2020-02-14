from talon.voice import Context, Str, press, Key

context = Context("vocabulary")

context.keymap({
    "pan dock": "pandoc",
    "P B copy": "pbcopy",
})
