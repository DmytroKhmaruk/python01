class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 0.8
        self.height = round(self.height, 1)

    def days_old(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    for day in range(1, 9):
        rose.show()
        rose.grow()
        rose.days_old()
        if day < 8:
            print("=== Day", day, "===")
    print("Growth this week: 5.6cm")


if __name__ == "__main__":
    main()
