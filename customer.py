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
        self.list = [self.full_name(), str(self.age), str(self.entry_fee())]

    def full_name(self):
        return f'{self.first_name} {self.family_name}'


    def entry_fee(self):
        if self.age < 20:
            return 1000
        if 20 <= self.age < 65:
            return 1500
        if self.age >= 65:
            return 1200

    def info_csv(self):
        list_csv = ",".join(self.list)  # .join()は文字列を結合する
        return list_csv


ken = Customer("Ken", "Tanaka", 15)
print(ken.full_name())
print(ken.age)
print(ken.entry_fee())
print(ken.info_csv())

tom = Customer("Tom", "Ford", 57)

ieyasu = Customer("Ieyasu", "Tokugawa", 73)
