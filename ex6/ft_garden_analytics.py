class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    @staticmethod
    def is_older_than_year(age_days: int) -> None:
        print(f"Is {age_days} more than a year? -> ", end='')
        if age_days > 365:
            print("True")
        else:
            print("False")


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


def main() -> None:
    print("=== Garden statistics ===")
    print("== Check years-old")
    Plant.is_older_than_year(30)
    Plant.is_older_than_year(400)
    print()

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


if __name__ == "__main__":
    main()
