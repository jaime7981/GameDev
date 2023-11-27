from classes.plant.plant import Plant

'''
Esta es una clase que hereda de Plant.
Esto significa que Cactus tiene todos los atributos y métodos de Plant.
'''

class Cactus(Plant):
    def __init__(self):
        super().__init__(
            cost=200,
            max_growth=100,
            growth_rate=0.08,
            health=500,
            water=10,
            sunlight=1
        )

        self.damage = 10

    def damage_plant(self, plant: Plant):
        plant.take_health(self.damage)
