#! python3
# mcb.pyw - saves and loads text fragments in clipboard
#
# Usage: py.exe mcb.pyw save <key_word> - saves content from clipboard with key_word
#        py.exe mcb.pyw <key_word> - loads text, corresponding to key_word in clipboard
#        py.exe mcb.pyw list - loads all key_word's in clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Saving content from clipboard
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # Forming list of key words and loading the content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
