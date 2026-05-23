class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age_days: int, color: str) -> None:
        super().__init__(name, height, age_days)
        self.color: str = color
        self.is_bloomed: bool = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self.is_bloomed:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")

    def bloom(self) -> None:
        self.is_bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age_days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter: float = trunk_diameter
        self.does_shade: bool = False

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        if self.does_shade:
            print(
                f" Tree {self.name} now produces a shade of"
                f"{self.height}cm long and {self.trunk_diameter}cm wide."
            )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age_days)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        self.height = round(self.height + 2.1, 1)
        self.nutritional_value += 1

    def age(self) -> None:
        self.age_days += 1


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    print("[asking the oak to produce shade]")
    oak.does_shade = True
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()

    print("[make tomato grow and age for 20 days]")
    for i in range(1, 21):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
