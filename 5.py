class Food:
    def __init__(self, name, ex_date, manufac):
        self.name = name
        self.expiration_date = ex_date
        self.manufac = manufac

    def hp(self):
        print(self.name, "from", self.manufac, "healed me by 0 hp")


obj = Food('Burger', 'Today', 'Bahandi')
obj.hp()

    
class Soup(Food):
    def __init__(self, name, ex_date, manufac, concentration):
        super().__init__( name, ex_date, manufac)
        self.concentration = concentration

    def hp_soup(self):
        print(self.name, "from", self.manufac, "thick", self.concentration, "healed me by 50 hp")

obj = Soup('lentil', 'yesterday', 'restaraunt', 'thick')
obj.hp_soup()

class Salad(Food):
    def __init__(self, name, ex_date, manufac, type):
        super().__init__(name, ex_date, manufac)
        self.type = type

       
class Main(Food):
    def __init__(self, name, ex_date, manufac, quaility):
        super().__init__(name, ex_date, manufac)
        self.quality = quaility


class Dessert(Food):
    def __init__(self, name, ex_date, manufac, type):
        super().__init__(name, ex_date, manufac)
        self.type = type