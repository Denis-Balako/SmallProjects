#! python3
# madLib.py - changes words in .txt files

import re


def main():
    originTextFile = open(r'F:\test\madLibTest.txt', encoding="utf8")
    originText = originTextFile.read()
    originTextFile.close()
    wordsList = originText.split()
    # searchWords = ['СУЩЕСТВИТЕЛЬНОЕ', 'ПРИЛАГАТЕЛЬНОЕ', 'ГЛАГОЛ']
    searchWordsRegex = re.compile(r'СУЩЕСТВИТЕЛЬНОЕ|ПРИЛАГАТЕЛЬНОЕ|ГЛАГОЛ')
    newText = ''

    for word in wordsList:
        mo1 = searchWordsRegex.search(word)
        if mo1:
            print('Введите ' + mo1.group().lower() + ':')
            newWord = input('> ')
            newWord = word.replace(mo1.group(), newWord)
            # re.sub(searchWordsRegex, newWord, word)
            newText += newWord + ' '
            continue
        else:
            newText += word + ' '

    newText.rstrip()
    endFile = open('madLibChangedText.txt', 'w')
    endFile.write(newText)
    endFile.close()
    print(newText)


if __name__ == '__main__':
    main()
