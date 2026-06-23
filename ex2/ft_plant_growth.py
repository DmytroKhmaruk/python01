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


def main():
    rose = Plant("Rose", 25.0, 30)
    grow = 0.8
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print("=== Day", day, "===")
        rose.grow(grow)
        rose.days_old(1)
        rose.show()
    print(f"Growth this week: {round((day * grow), 1)}cm")


if __name__ == "__main__":
    main()
