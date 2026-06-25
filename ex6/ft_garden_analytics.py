#! /usr/bin/env python3
class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def show(self) -> None:
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, "
                f"{self.show_calls} show"
            )

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.stats = Plant.Stats()

    def grow(self, height: float) -> None:
        self.stats.grow_calls += 1
        self.height += height
        self.height = round(self.height, 1)

    def age(self, days: int) -> None:
        self.stats.age_calls += 1
        self.days += days

    def show(self) -> None:
        self.stats.show_calls += 1
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    @staticmethod
    def is_older(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
            self, name: str, height: float, days: int,
            color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True
        self.show()


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

        def show(self) -> None:
            super().show()
            print(f" {self.shade_calls} shade")

    def __init__(
            self, name: str, height: float, days: int, trunk_diameter: float
            ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
        self.stats: Tree.TreeStats = Tree.TreeStats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.stats.shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of {self.height}cm long"
            f" and {self.trunk_diameter}cm wide.")


class Seed(Flower):
    def __init__(
            self, name: str, height: float, days: int, color: str,
            seeds: int) -> None:
        super().__init__(name, height, days, color)
        self.seeds = seeds
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.show()


def main() -> None:
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunfl = Seed("Sunflower", 80.0, 45, "yellow", 0)

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older(400)}")

    print("\n=== Flower")
    Flower.show(rose)
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    display_statistics(rose)

    print("\n=== Tree")
    Tree.show(oak)
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    Seed.show(sunfl)
    print("[make sunflower grow, age and bloom]")
    sunfl.seeds += 42
    sunfl.age(20)
    sunfl.grow(30)
    sunfl.bloom()
    display_statistics(sunfl)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    main()
