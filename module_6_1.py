# alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
class Animal:

    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed


class Mammal (Animal):

    def eat(self, food):
        if isinstance(food, Plant):
            # если растение съедобное
            if food.edible:
                print(f'{self.name}, съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name}, не стал есть {food.name}')
                self.alive = False
        else:
            print(f'{food.name} не является растением. {self.name} не может это съесть.')


class Predator (Animal):

    def eat(self, food):
        if isinstance(food, Plant):
            # если растение съедобное
            if food.edible:
                print(f'{self.name}, съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name}, не стал есть {food.name}')
                self.alive = False
        else:
            print(f'{food.name} не является растением. {self.name} не может это съесть.')

# edible = False(съедобность), name - индивидуальное название каждого растения


class Plant:

    def __init__(self, name, edible=False):
        self.edible = edible
        self.name = name


class Flower(Plant):

    def __init__(self, name):
        super().__init__(name, edible=False)


class Fruit(Plant):
    
    def __init__(self, name):
        super().__init__(name, edible=True)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)