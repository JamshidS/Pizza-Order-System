import csv
import datetime


class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 10.0)


class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza ", 12.0)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turk Pizza ", 15.0)


class DominosPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza ", 8.0)


class Decorator:
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return str(self.component.get_cost() + Pizza.get_cost(self))

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Zeytin Sos"
        self._cost = 1.0

    def get_cost(self):
        return self._cost + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


class Mantarlar(Decorator):
    def __init__(self, component):
        super().__init__(self, component)
        self._description = "Mantarlar Sos"
        self._cost = 1.0

    def get_cost(self):
        return self._cost + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(self, component)
        self._description = "KeciPeyniri Sos"
        self._cost = 2.0

    def get_cost(self):
        return self._cost + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Et Sos"
        self._cost = 2.5

    def get_cost(self):
        return self._cost + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Soğan Sos"
        self._cost = 1.0

    def get_cost(self):
        return self._cost + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Mısır Sos"
        self._cost = 1.0

    def get_cost(self):
        return self._cost + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ' ' + self._description


def main():
    with open('Menu.txt', 'r') as f:
        print(f.read())

    pizza_choices = {
        "klasik": KlasikPizza(),
        "margarita": MargaritaPizza(),
        "turk": TurkPizza(),
        "dominos": DominosPizza(),
    }

    while True:
        pizza_choice = input("luten istediginiz pizzayi seciniz: ").lower()
        if pizza_choice in pizza_choices:
            pizza = pizza_choices[pizza_choice]
            break
        else:
            print("Yanlis secim yaptiniz...")

    sauce_choices = {
        "zeytin": Zeytin,
        "mantarlar": Mantarlar,
        "keci peyniri": KeciPeyniri,
        "et": Et,
        "sogan": Sogan,
        "misir": Misir,
    }

    while True:
        sauce_choice = input(
            "Sos seçiniz (Zeytin, Mantarlar, KeciPeyniri, Et, Sogan, Misir) ya da bitirmek için 'bittir' yazınız: ").lower()
        if sauce_choice == "bittir":
            break
        elif sauce_choice in sauce_choices:
            pizza = sauce_choices[sauce_choice](pizza)
        else:
            print("Invalid input. Please select a valid sauce.")

    total_cost = pizza.get_cost()
    name = input("Isminiz lutfen: ")
    tc_number = input("TC Kimlik numaranizi giriniz: ")
    credit_card_number = input("kredi kart numaraniz lutfen: ")
    credit_card_pin = input("Kredi Kart sifreniz lutfen: ")

    with open('Orders_Database.csv', encoding='utf-8', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [pizza.get_description(), name, tc_number, credit_card_number, total_cost, datetime.datetime.now(),
             credit_card_pin])

    print("Order placed successfully. total cost: " + str(total_cost))


main()
