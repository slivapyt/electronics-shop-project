from src.item import Item


class MixinLog():

    def __init__(self):
        self.__current_lang = "EN"
        self.eng = "RU"
        self.rus = "EN"

    @property
    def language(self):
        return self.__current_lang

    def change_lang(self):
        if self.__current_lang == self.eng:
            self.__current_lang = self.rus
        else:
            self.__current_lang = self.eng


class Keyboard(Item, MixinLog):
    pass
