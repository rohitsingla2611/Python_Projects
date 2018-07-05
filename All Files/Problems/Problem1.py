class Juggler:
    def __init__(self, name):
        self.name = name

    def juggles(self, juggling_item):
        print(self.name + ' perform juggles ' + juggling_item.get_name())


class JugglingItem:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


Juggler1 = Juggler('TOM')
Juggler2 = Juggler('Banku')
JugglingItem1 = JugglingItem('Knife')
JugglingItem2 = JugglingItem('Torch')
Juggler1.juggles(JugglingItem1)
Juggler2.juggles(JugglingItem2)
