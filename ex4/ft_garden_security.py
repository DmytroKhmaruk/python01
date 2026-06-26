#! /usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"\n{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"\nHeight updated: {round(self._height)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(
            f"Plant created: {self.name}: "
            f"{self.get_height()}cm, "
            f"{self.get_age()} days old"
        )


def main() -> None:
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    rose.show()

    rose.set_height(25.0)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-10)

    print(
        f"\nCurrent state: {rose.name}: "
        f"{rose._height}cm, "
        f"{rose._age} days old"
          )


if __name__ == "__main__":
    main()
