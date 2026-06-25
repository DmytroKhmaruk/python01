#! /usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self, height: float) -> None:
        self.height += height
        self.height = round(self.height, 1)

    def age(self, days: int) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        self.days += days

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height}cm, {self.days} days old")


class Flower(Plant):
    def __init__(
            self, name: str, height: float, age: int, color: str
            ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False
        self.flower = True

    def show(self) -> None:
        if self.flower:
            print("=== Flower")
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name.capitalize()} is blooming beautifully!\n")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True
        self.flower = False
        print(f"[asking the {self.name} to bloom]")
        self.show()


class Tree(Plant):
    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        print("=== Tree")
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name.capitalize()} "
            f"now produces a shade of {self.height}cm long"
            f" and {self.trunk_diameter}cm wide.\n")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float, age: int,
            harvest_season: str, nutritional_value: int
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.vegetable = True

    def show(self,) -> None:
        if self.vegetable:
            print("=== Vegetable")
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")
        self.vegetable = False


def main() -> None:
    rose = Flower("rose", 15.0, 10, "red")
    oak = Tree("oak", 200.0, 365, 5.0)
    tomato = Vegetable("tomato", 5.0, 10, "April", 0)
    print("=== Garden Plant Types ===")
    Flower.show(rose)
    rose.bloom()
    Tree.show(oak)
    oak.produce_shade()
    Vegetable.show(tomato)
    tomato.grow(42)
    tomato.age(20)
    tomato.nutritional_value += 20
    Vegetable.show(tomato)


if __name__ == "__main__":
    main()
