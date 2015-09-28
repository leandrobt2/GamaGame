from enum import Enum, unique
import random

@unique
class PlayType(Enum):
    english_portuguese = 1
    portuguese_english = 2

words = []


class Word:
    def __init__(self, portuguese, english):
        self.__portuguese = portuguese
        self.__english = english

    def get_portuguese(self):
        return self.__portuguese

    def get_english(self):
        return self.__english

    def list_words(self):
        return self.__english

    def __str__(self):
        return "The word in english is:{0} and in portuguese {1}".format(self.__english, self.__portuguese)


def choose():
    print_line()
    print('Choose an option')
    print('1) Insert new word')
    print('2) Play Portuguese -> English')
    print('3) Play English -> Portuguese')
    print('4) Exit')
    print_line()

    option = int(input('Choose an option'))
    if option < 1 or option > 4:
        print('Oops, it looks like you entered a invalid value')
        choose()

    if option == 1:
        add()
    elif option == 2:
        start(PlayType.portuguese_english)
    elif option == 3:
        start(PlayType.english_portuguese)
    else:
        exit()


def list_words():
    for word in words:
        print(word)


def add():
    while True:
        print('Type -1 to stop to add words')

        portuguese = input('type a portuguese word')
        if portuguese == '-1':
            break

        english = input('type an english word')
        if english == '-1':
            break

        duplicated = False
        for word in words:
            if word.get_portuguese() == portuguese and word.get_english() == english:
                print('Sorry dude, that word already exists on list')
                print_line()
                duplicated = True
                continue

        if not duplicated:
            words.append(Word(portuguese, english))

        print_line()

    list_words()
    choose()


def start(playtype):
    print_line()

    if len(words) <= 3:
        print('Ouch, it looks like you have not added the amount of word needed')
        choose()

    print('Welcome bro, your are going to play in ' + str(playtype) + ' type, enjoy it :)')
    print('Type -1 any time to go back to menu')
    print_line()

    question_word = get_question_word()
    internal_words = get_randon_words(question_word)

    if playtype == PlayType.english_portuguese:
        print('The word in english {0} means which in portuguese:'.format(question_word.get_english()))
    else:
        print('The word in portuguese {0} means which in english:'.format(question_word.get_portuguese()))

    random.shuffle(internal_words)

    for i in range(0, len(internal_words)):
        if playtype == PlayType.english_portuguese:
            print(str(i)+")"+internal_words[i].get_portuguese())
        else:
            print(str(i)+")"+internal_words[i].get_english())

    result = int(input())
    if result == -1:
        choose()

    if internal_words[result].get_portuguese() == question_word.get_portuguese() and \
        internal_words[result].get_english() == question_word.get_english():
        print('Nice shoot')
    else:
        print('Sorry to say it, but you are wrong, =/')

    start(playtype)


def get_question_word():
    min = 0
    max = len(words) - 1
    rand = random.randint(min, max)
    return words[rand]


def get_randon_words(word):
    min = 0
    max = len(words) - 1
    internal_words = [word]
    while len(internal_words) < 4:
        rand = random.randint(min, max)
        temp_random_word = words[rand]
        exists = False
        for internal_word in internal_words:
            if internal_word.get_portuguese() == temp_random_word.get_portuguese() and internal_word.get_english() == temp_random_word.get_english():
                exists = True
                break
            else:
                continue

        if not exists:
            internal_words.append(temp_random_word)

    return internal_words


def exit():
    print('Thanks to play it, Good bye ;)')


def print_line():
    print('-'*25)

if __name__ == '__main__':
    choose()
