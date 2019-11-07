"""
C-1. フルネームを取得できる
ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す

tom = Customer(first_name="Tom", family_name="Ford")
tom.full_name()  # "Tom Ford" という値を返す
"""


class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        print(f'NAME:{self.first_name} {self.family_name}, AGE:{self.age}')

    def entry_fee(self):
        if self.age < 20:
            print('1000円')
        if 20 <= self.age < 65:
            print('1500円')
        if self.age >= 65:
            print('1200円')


ken = Customer("Ken", "Tanaka", 15)
ken.full_name()
ken.entry_fee()

tom = Customer("Tom", "Ford", 57)
tom.full_name()
tom.entry_fee()

ieyasu = Customer("Ieyasu", "Tokugawa", 73)
ieyasu.full_name()
ieyasu.entry_fee()
