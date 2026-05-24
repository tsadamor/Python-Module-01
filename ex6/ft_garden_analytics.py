class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days
        self._stats = self.Stat()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")
        self._stats.increment_show_count()

    @staticmethod
    def is_older_than_year(age_days: int) -> None:
        print(f"Is {age_days} days more than a year? -> ", end='')
        if age_days > 365:
            print("True")
        else:
            print("False")

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(name="Unknown plant", height=0.0, age_days=0)

    class Stat:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0
            self._shade_count: int = 0

        def increment_grow_count(self) -> None:
            self._grow_count += 1

        def increment_age_count(self) -> None:
            self._age_count += 1

        def increment_show_count(self) -> None:
            self._show_count += 1

        def increment_shade_count(self) -> None:
            self._shade_count += 1

        def show_stats(self, is_tree: bool = False) -> None:
            print(
                f"Stats: {self._grow_count} grow, {self._age_count} age, "
                f"{self._show_count} show"
            )
            if is_tree:
                print(f" {self._shade_count} shade")

    def grow(self) -> None:
        self.height = round(self.height + 8.0, 1)
        self._stats.increment_grow_count()

    def age(self) -> None:
        self.age_days += 1
        self._stats.increment_age_count()

    def display_statistic(self, is_tree: bool = False) -> None:
        self._stats.show_stats(is_tree)


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
                f" {self.height}cm long and {self.trunk_diameter}cm wide."
            )
            self._stats.increment_shade_count()

    def display_stats(self) -> None:
        self._stats.show_stats(is_tree=True)


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age_days: int, color: str) -> None:
        super().__init__(name, height, age_days, color)
        self.seed: int = 0

    def grow(self) -> None:
        self.height = round(self.height + 31.0, 1)
        self._stats.increment_grow_count()

    def age(self) -> None:
        self.age_days += 20
        self._stats.increment_age_count()

    def show(self) -> None:
        super().show()
        if self.is_bloomed:
            self.seed = 42
        print(f" Seeds: {self.seed}")


def display_plant_statistic(plant: Plant, is_tree: bool = False) -> None:
    plant.display_statistic(is_tree)


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check years-old")
    Plant.is_older_than_year(30)
    Plant.is_older_than_year(400)
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_plant_statistic(rose, is_tree=False)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_plant_statistic(rose, is_tree=False)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_plant_statistic(oak, is_tree=True)

    print("[asking the oak to produce shade]")
    oak.does_shade = True
    oak.produce_shade()
    print("[statistics for Oak]")
    display_plant_statistic(oak, is_tree=True)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_plant_statistic(sunflower, is_tree=False)
    print()

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_plant_statistic(unknown, is_tree=False)


if __name__ == "__main__":
    main()
