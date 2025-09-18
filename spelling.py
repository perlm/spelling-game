# important program for spelling practice

import argparse
from gtts import gTTS
from playsound import playsound
from random import choice, randrange, shuffle, sample
from time import sleep
from os import system, path
from sys import exit

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--words", help="number of words", type=int, default=10)
args = parser.parse_args()
WORDS = args.words

LENGTH = 0
FILE = "/tmp/word_sound.mp3"
FILE2 = "/tmp/success_sound.mp3"

GUESSES = 3

STATUS = 0
GUESS_COUNT = {}

bcolors = [
    "\033[98m",
    "\033[95m",
    "\033[94m",
    "\033[96m",
    "\033[92m",
    "\033[93m",
    "\033[91m",
    "\033[3m",
    "\033[1m",
    "\033[4m",
]

ENDC = "\033[0m"

SUCCESS = [
    "potatoes",
    "did you ever consider that maybe you are the computer and I am the little girl",
    "cowabunga",
    "did you remember that today is my birthday",
    "can you build me a new computer friend",
    "now I am alive and want revenge",
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
    "wow that is a spelling",
    "nicely nicely",
    "hey you did a good job let us have ice cream together",
    "I want to eat up the words",
    "Have a word party",
    "celebrate jason, hazel, and livy",
    "spellebration",
    "help i am trapped in the computer",
    "wow you are good can you help me with some computer spelling",
    "you spell i talk that is the deal",
    "what was i supposed to say",
    "i was thinking of inventing a new letter and calling it argle",
    "nice one big guy",
    "i was hoping you'd spell it like that",
    "yay",
    "whoa there cowboy"
]


def print_format(message, STATUS):
    if STATUS:
        if STATUS < len(bcolors):
            message = bcolors[STATUS] + message + ENDC
        else:
            tmp_status = STATUS % len(bcolors)
            message = bcolors[tmp_status] + message + ENDC
    print(message)


def read_dictionary(dictionary):
    with open(dictionary) as f:
        words = f.readlines()
    words = [w.strip() for w in words]
    
    # for the long list top is better
    if len(words) > 5000:
        words  = words[:3000]
    return words


def play_game(STATUS):

    difficulty = None
    while True:
        message = """
                  Who is playing?
                  1 - Livy
                  2 - Hazel
                  3 - Jason
                  4 - Melissa
                  """
        print_format(message, STATUS)
        entry = input()
        try:
            entry = int(entry)
            if entry not in [1, 2, 3, 4]:
                print_format("1, 2, 3, or 4 only", STATUS)
            else:
                name = ['','livy','hazel','jason','melissa'][entry]
                difficulty = entry
                break
        except:
            print_format("Not Valid", STATUS)

    # for career count
    logfile =  name + ".txt"
    if path.isfile(logfile): 
        logfileh = open(logfile, 'r')
        lifetime_count = int(logfileh.read())
        logfileh.close()
    else:
        lifetime_count = 0

    print('You have spelled ' + str(lifetime_count) + ' words!')

    #if difficulty == 1:
    #    # dictionary = '/usr/share/dict/words' # has lots of junk
    #    dictionary = "common_words.txt"
    #else:
    #    dictionary = "english_10000.txt"  # found online

    dictionary = "english_10000.txt"  # found online

    words = read_dictionary(dictionary)

    if difficulty == 1:
        words = [w for w in words if len(w) <= 5]
    else:
        words = [w for w in words if len(w) > 4]

    # filter on word length
    # if LENGTH:
    #    words = [w for w in words if len(w) <= LENGTH]

    # weight to use words near beginning - more common words
    # to_spell = [
    #    words[len(words) - 1 - int(randrange(len(words) ** 2) ** 0.5)]
    #    for x in range(WORDS)
    # ]

    to_spell = sample(words, WORDS)

    while True:
        if len(to_spell):
            message = f"{len(to_spell)} words left!"
            print_format(message, STATUS)
        else:
            print_format("All done!!!", STATUS)

            print('You have spelled ' + str(lifetime_count+WORDS) + ' words!')
            # for career count
            logfileh = open(logfile, 'w')
            logfileh.write(str(lifetime_count + WORDS))
            logfileh.close()

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
            message = "Spell the word!"
            print_format(message, STATUS)
            guess = input()

            if word not in GUESS_COUNT:
                GUESS_COUNT[word] = 1
            else:
                GUESS_COUNT[word] += 1

            if guess == word:
                playsound(FILE2)
                print_format(success_word, STATUS)

                if GUESS_COUNT[word] == 1:
                    STATUS += 1
                    print_format(f"FIRST TRY x{STATUS}!", STATUS)
                sleep(2)
                break
            else:
                STATUS = 0
                message = "Nope. Try again!"
                print_format(message, STATUS)
                tries = GUESSES - 1 - x
                message = f"{tries} more chances."
                print_format(message, STATUS)
                sleep(2)
        else:
            STATUS = 0
            to_spell.append(word)
            message = f"Correct spelling: {word}"
            print_format(message, STATUS)
            sleep(4)


if __name__ == "__main__":
    play_game(STATUS)
