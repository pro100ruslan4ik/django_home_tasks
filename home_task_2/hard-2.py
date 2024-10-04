class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)

class CartoonToy(Toy):
    def __init__(self, name, color):
        super().__init__(name,color)


class ToyFabric:
    def create_toy(self, name, color, toy_type):
        self.purchase_materials()
        self.sew_toy()
        self.paint_toy(color)
        print()

        if toy_type == "Животное":
            return AnimalToy(name, color)
        elif toy_type == "Персонаж мультфильма":
            return CartoonToy(name, color)


    def purchase_materials(self):
        print("Закупка материалов...")

    def sew_toy(self):
        print("Шьем игрушку...")

    def paint_toy(self, color):
        print("Окрашиваем игрушку в " + color + "...")

tf = ToyFabric()

first_toy = tf.create_toy("Плюшевый медведь", "Коричневый", "Животное")
second_toy = tf.create_toy("Плюшевый Лунтик", "Розовый", "Персонаж мультфильма")

