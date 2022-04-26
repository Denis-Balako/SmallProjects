"""Сообщение в виде битовой карты, (с) Денис Балако denisarius2000s@gmail.com
Отображает текстовое сообщение в соответствии с указаной битовой картой.

Теги: крошечная, графика
"""

import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('''Bitmap Message by Denis Balako denisarius2000s@gmail.com''')
print('Enter the message to display with the bitmap')
message = input('> ')
if message == '':
    sys.exit()

# Проходим в цикле по всем строкам битовой карты
for line in bitmap.splitlines():
    # Проходим в цикле по всем символам строки
    for i, bit in enumerate(line):
        if bit == ' ':
            # Выводим пустое пространство согласно пробелу на битовой карте
            print(' ', end='')
        else:
            # Выводим символ сообщения
            print(message[i % len(message)], end='')
    # Выводим символ новой строки
    print()
