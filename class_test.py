# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 80}
#
#
# def print_role(role):
#     print('name is {}, hp is {}'.format(role['name'], role['hp']))
#
#
# print_role(user1)


class Player:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def print_role(self):
        print('{}: {}'.format(self.name, self.hp))

    def _print_abc(self):
        print('abc')


user1 = Player('tom', 100)
user2 = Player('jerry', 99)
user1.print_role()
user2.print_role()

Player.print_role(user1)
Player.print_abc(user1)
