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
        self.days += days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    grow = 0.8
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print("=== Day", day, "===")
        rose.grow(grow)
        rose.age(1)
        rose.show()
    print(f"Growth this week: {round((day * grow), 1)}cm")


if __name__ == "__main__":
    main()
