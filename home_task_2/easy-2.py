class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name + " поехала...")

    def stop(self):
        print(self.name + " остановилась...")

    def turn(self,direction):
        print(self.name + " повернула " + direction + "...")


class TownCar(Car):
    def __init__(self):
        super().__init__(60, "Красный", "Городская машина", False)


class SportCar(Car):
    def __init__(self):
        super().__init__(120, "Желтый", "Спортивная машина", False)


class WorkCar(Car):
    def __init__(self):
        super().__init__(60, "Белый", "Рабочая машина", False)


class PoliceCar(Car):
    def __init__(self):
        super().__init__(80, "Синий", "Полицейская машина", True)


police_car = PoliceCar()
police_car.go()
police_car.turn("налево")
police_car.stop()
