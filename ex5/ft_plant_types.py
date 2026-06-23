class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, height):
        self.height += height
        self.height = round(self.height, 1)

    def days_old(self, age):
        self.age += age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, color):
        self.color = color


class Tree(Plant):
    def __init__(self, trunk_diameter):
        self.trunk_diameter = trunk_diameter


class Vegetable(Plant):
    def __init__(self, harvest_season, nutritional_value):
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def main():
    rose = Plant("Rose", 15.0, 10)
    oak = Plant("Oak", 200.0, 365)
    tomato = Plant("Tomato", 5.0, 10)
    print("=== Garden Plant Types ===")
    rose.show()
    oak.show()
    tomato.show()


if __name__ == "__main__":
    main()
