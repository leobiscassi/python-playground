'''
    @codewars - https://www.codewars.com/kata/591588d49f4056e13f000001
    Date: 02/02/2020
    Author: Léo Biscassi
'''
import sys


def HQ9(code):
    msg = None
    if code == 'H':
        msg = 'Hello World!'
    elif code == 'Q':
        msg = code
    elif code == '9':
        msg = sing_song()
    return msg


def sing_song():
    bottles = list(range(1, 100))
    bottles = bottles[::-1]
    song = []

    for bottle in bottles:
        if bottle > 2:
            phrase = f'{bottle} bottles of beer on the wall, {bottle} bottles of beer.\nTake one down and pass it around, {bottle-1} bottles of beer on the wall.'
            song.append(phrase)
        elif bottle == 2:
            phrase = f'{bottle} bottles of beer on the wall, {bottle} bottles of beer.\nTake one down and pass it around, {bottle-1} bottle of beer on the wall.'
            song.append(phrase)
        elif bottle == 1:
            phrase = f'{bottle} bottle of beer on the wall, {bottle} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
            song.append(phrase)

    return "\n".join(song)


if __name__ == '__main__':
    code = sys.argv[1]
    print(HQ9(code))
