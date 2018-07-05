class CircusAnimal:
    def eat(self, food):
        print('Eat Daily', food)

    def sleep(self, hours):
        print('')


class Monkey(CircusAnimal):

    def eat(self, medicine, food):
        super().eat(food)
        print('and Eat medicine', medicine)


m = Monkey()
m.eat('crocin', 'ff')
