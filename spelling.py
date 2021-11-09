# important program for spelling practice

from gtts import gTTS
from playsound import playsound
from random import choice, randrange, shuffle
from time import sleep
from os import system
from sys import exit

LENGTH = 0
FILE = "/tmp/word_sound.mp3"
FILE2 = "/tmp/success_sound.mp3"
# DICTIONARY = '/usr/share/dict/words' # has lots of junk
DICTIONARY = "common_words.txt"  # found online

GUESSES = 3
WORDS = 10

SUCCESS = [
    "look out",
    "spell " * 10,
    "what up spelling",
    "spelling " * 10,
    "watch it",
    "good job",
    "way to be",
    "you know it",
    "nice work",
    "keep it up",
    "wowzers",
    "big time",
    "party time",
    "good spelling",
    "you got it",
    "yeah yeah yeah",
    "spelling",
    "yes that is right",
    "way to spell",
    "now you are spelling",
    "keep spelling",
    "nice spelling",
    "look out",
    "it is spelling time",
    "spell spell spell",
    "hey it is me spelling computer nice work",
    "go spell it",
    "look out for spelling",
    "you smell but good spelling",
    "spell more",
    "yes that is spelling",
    "you good spell",
    "ice cream time for me the computer",
    "spell more or no treats",
    "whoa there",
    "ahoy spelling",
    "wow that is a spelling"
    "nicely nicely"
]


def read_dictionary():
    with open(DICTIONARY) as f:
        words = f.readlines()
    words = [w.strip() for w in words]
    return words


def play_game():
    words = read_dictionary()

    # filter on word length
    if LENGTH:
        words = [w for w in words if len(w) <= LENGTH]

    # weight to use words near beginning - more common words
    to_spell = [
        words[len(words) - 1 - int(randrange(len(words) ** 2) ** 0.5)]
        for x in range(WORDS)
    ]

    while True:
        if len(to_spell):
            print(f"{len(to_spell)} words left!")
        else:
            print("All done!!!")
            sleep(3)
            exit()

        shuffle(to_spell)

        word = to_spell.pop()

        my_aud = gTTS(word)
        my_aud.save(FILE)
        success_word = choice(SUCCESS)
        my_aud = gTTS(success_word)
        my_aud.save(FILE2)

        for x in range(GUESSES):
            playsound(FILE)

            system("clear")
            print("Spell the word!")
            guess = input()
            if guess == word:
                playsound(FILE2)
                print(success_word)
                sleep(3)
                break
            else:
                print("Nope. Try again!")
                tries = GUESSES - 1 - x
                print(f"{tries} more chances.")
                sleep(2)
        else:
            to_spell.append(word)
            print(f"Correct spelling: {word}")
            sleep(3)


if __name__ == "__main__":
    play_game()
