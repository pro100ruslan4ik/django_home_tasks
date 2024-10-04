class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type



class ToyFabric:
    def create_toy(self, name, color, toy_type):
        self.purchase_materials()
        self.sew_toy()
        self.paint_toy(color)
        print()
        return Toy(name, color, toy_type)


    def purchase_materials(self):
        print("Закупка материалов...")

    def sew_toy(self):
        print("Шьем игрушку...")

    def paint_toy(self, color):
        print("Окрашиваем игрушку в " + color + "...")


tf = ToyFabric()

first_toy = tf.create_toy("Плюшевый медведь", "Коричневый", "Животное")
second_toy = tf.create_toy("Плюшевый Лунтик", "Розовый", "Персонаж мультфильма")

