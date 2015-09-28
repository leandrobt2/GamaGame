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