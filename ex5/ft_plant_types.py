class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, height: float) -> None:
        self.height += height
        self.height = round(self.height, 1)

    def days_old(self, age: int) -> None:
        print(f"[make {self.name.lower()} grow and age for {age} days]")
        self.age += age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


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
            print(f" {self.name} is blooming beautifully!\n")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True
        self.flower = False
        print(f"[asking the {self.name.lower()} to bloom]")
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
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self.height}cm long"
            f"and {self.trunk_diameter}cm wide.\n")


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
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Garden Plant Types ===")
    Flower.show(rose)
    rose.bloom()
    Tree.show(oak)
    oak.produce_shade()
    Vegetable.show(tomato)
    tomato.grow(42)
    tomato.days_old(20)
    tomato.nutritional_value += 20
    Vegetable.show(tomato)


if __name__ == "__main__":
    main()
