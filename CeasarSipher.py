#! python3

"""Ceasar Cipher, Denis Balako denisarius2000s@gmail.com
Tags: short, for beginners, crypto"""

try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Ceasar Cipher by Denis Balako denisarius2000s@gmail.com')
print('The Ceasar cipher encypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# Asks if user want to encrypt or decrypt
while True:
    print('Do you want (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Enter the message to {}'.format(mode))
message = input('> ')
message = message.upper()
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)
        translated += SYMBOLS[num]
    else:
        translated += symbol
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass
