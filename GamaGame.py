from enum import Enum, unique
from Word import Word
import random

@unique
class PlayType(Enum):
    english_portuguese = 1
    portuguese_english = 2

class GamaGame:

    def __init__(self):
        self.words = []
        self.total_plays = 0
        self.total_right = 0

    def check_score(self):
        if self.total_plays == 0:
            print('You can not check the score without a first try')
            return

        display_str1 = "You've played {0} times.".format(self.total_plays)
        display_str2 = "You hit the target {0} times. Which is {1}%".format(self.total_right,
                                                                            (self.total_right * 100) / self.total_plays)
        display_str3 = "You missed {0} times. Which is {1}%".format(self.total_plays - self.total_right, ((self.total_plays - self.total_right) * 100) / self.total_plays)

        print(display_str1)
        print(display_str2)
        print(display_str3)

    def choose(self):
        self.print_line()
        print('Choose an option')
        print('1) Insert new word')
        print('2) List all words')
        print('3) Play Portuguese -> English')
        print('4) Play English -> Portuguese')
        print('5) Check Score')
        print('6) Exit')
        self.print_line()

        option = int(input('Choose an option'))
        if option < 1 or option > 6:
            print('Oops, it looks like you entered a invalid value')
            self.choose()

        if option == 6:
            self.exit()

        if option == 1:
            self.add()
        elif option == 2:
            self.list_words()
        elif option == 3:
            self.start(PlayType.portuguese_english)
        elif option == 4:
            self.start(PlayType.english_portuguese)
        else:  # option is 5
            self.check_score()

        self.choose()

    def list_words(self):
        for word in self.words:
            print(word)

    def add(self):
        while True:
            print('Type -1 to stop to add words')

            portuguese = input('type a portuguese word')
            if portuguese == '-1':
                break

            english = input('type an english word')
            if english == '-1':
                break

            duplicated = False
            for word in self.words:
                if word.get_portuguese() == portuguese and word.get_english() == english:
                    print('Sorry dude, that word already exists on list')
                    self.print_line()
                    duplicated = True
                    continue

            if not duplicated:
                self.words.append(Word(portuguese, english))

            self.print_line()

        return

    def start(self,playtype):
        self.print_line()

        if len(self.words) <= 3:
            print('Ouch, it looks like you have not added the amount of word needed')
            self.choose()

        print('Welcome bro, your are going to play in ' + str(playtype) + ' type, enjoy it :)')
        print('Type -1 any time to go back to menu')
        self.print_line()

        question_word = self.get_question_word()
        internal_words = self.get_randon_words(question_word)

        if playtype == PlayType.english_portuguese:
            print('Which the word in english \'{0}\' means in portuguese:'.format(question_word.get_english()))
        else:
            print('A palavra em Portugues \'{0}\' siguinifica o que em ingles?:'.format(question_word.get_portuguese()))

        random.shuffle(internal_words)

        for i in range(0, len(internal_words)):
            if playtype == PlayType.english_portuguese:
                print(str(i) + ")" + internal_words[i].get_portuguese())
            else:
                print(str(i) + ")" + internal_words[i].get_english())

        result = int(input())
        if result == -1:
            return

        self.total_plays = self.total_plays + 1

        if internal_words[result].get_portuguese() == question_word.get_portuguese() and \
                        internal_words[result].get_english() == question_word.get_english():
            print('Nice shoot')
            self.total_right = self.total_right + 1
        else:
            print('Sorry to say it, but you are wrong, =/')

        self.start(playtype)

    def get_question_word(self):
        min = 0
        max = len(self.words) - 1
        rand = random.randint(min, max)
        return self.words[rand]

    def get_randon_words(self, word):
        min = 0
        max = len(self.words) - 1
        internal_words = [word]
        while len(internal_words) < 4:
            rand = random.randint(min, max)
            temp_random_word = self.words[rand]
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

    def seed(self):
        self.words.append(Word('azul', 'blue'))
        self.words.append(Word('amarelo', 'yellow'))
        self.words.append(Word('verde', 'green'))
        self.words.append(Word('preto', 'black'))

    def print_line(self):
        print('-' * 25)

    def exit(self):
        print('Thanks to play it, Good bye ;)')