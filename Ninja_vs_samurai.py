Position = {'high': 'h', 'low': 'l'}  # needed for hard coded tests


class Warrior(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.block = ''
        self.deceased = self.zombie = False

    @staticmethod
    def attack(enemy, position):
        damage = 0
        if enemy.block != position:
            damage += (5, 10)[position == 'h']
        if enemy.block == '':
            damage += 5
        enemy.set_health(enemy.health - damage)

    def set_health(self, new_health):
        if new_health == 0:
            self.deceased = True
            self.zombie = False
        elif self.deceased:
            self.zombie = True
        self.health = max(0, new_health)
2 weeks agoRefactorDiscuss
5 kyu
Maximum subarray sum
Python:
def max_sequence(arr):
    """ max_sequence == PEP8 (forced mixedCase by CodeWars) """
    maximum = total = 0
    for a in arr:
        total = max(0, total + a)
        if total > maximum:
            maximum = total
    return maximum
