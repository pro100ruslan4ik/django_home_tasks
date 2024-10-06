class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def calculate_damage(self, enemy):

        effective_damage = self.damage - enemy.armor
        return max(0, effective_damage)

    def attack(self, enemy):
        damage_dealt = self.calculate_damage(enemy)
        enemy.health -= damage_dealt
        print(f"{self.name} атакует {enemy.name} и наносит {damage_dealt:.2f} урона.")
        print(f"У {enemy.name} осталось {enemy.health:.2f} здоровья.\n")


class Player(Person):
    def __init__(self, name="Игрок", health=100, damage=30, armor=20):
        super().__init__(name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name="Враг", health=80, damage=25, armor=10):
        super().__init__(name, health, damage, armor)


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):

        turn = self.player

        while self.player.health > 0 and self.enemy.health > 0:
            if turn == self.player:
                self.player.attack(self.enemy)
                turn = self.enemy
            else:
                self.enemy.attack(self.player)
                turn = self.player


            if self.player.health <= 0:
                print(f"{self.player.name} проиграл бой!")
            elif self.enemy.health <= 0:
                print(f"{self.enemy.name} побежден!")


player = Player()
enemy = Enemy()


game = Game(player, enemy)
game.start_battle()
