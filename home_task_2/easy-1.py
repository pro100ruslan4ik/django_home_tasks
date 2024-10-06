class TownCar:
    def __init__(self):
        self.speed = 60
        self.color = "Красный"
        self.name = "Городская машина"
        self.is_police = False

    def go(self):
        print(self.name + " поехала...")

    def stop(self):
        print(self.name + " остановилась...")

    def turn(self,direction):
        print(self.name + " повернула " + direction + "...")


class SportCar:
    def __init__(self):
        self.speed = 120
        self.color = "Желтый"
        self.name = "Спортивная машина"
        self.is_police = False

    def go(self):
        print(self.name + " поехала...")

    def stop(self):
        print(self.name + " остановилась...")

    def turn(self, direction):
        print(self.name + " повернула " + direction + "...")


class WorkCar:
    def __init__(self):
        self.speed = 60
        self.color = "Белый"
        self.name = "Рабочая машина"
        self.is_police = False

    def go(self):
        print(self.name + " поехала...")

    def stop(self):
        print(self.name + " остановилась...")

    def turn(self,direction):
        print(self.name + " повернула " + direction + "...")


class PoliceCar:
    def __init__(self):
        self.speed = 80
        self.color = "Синий"
        self.name = "Полицейская машина"
        self.is_police = True

    def go(self):
        print(self.name + " поехала...")

    def stop(self):
        print(self.name + " остановилась...")

    def turn(self,direction):
        print(self.name + " повернула " + direction + "...")



police_car = PoliceCar()
police_car.go()
police_car.turn("налево")
police_car.stop()