class Plant:
    name: str
    height: float
    days_old: int

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days_old} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days_old = 30

    rose.show()

    initial_height: float = rose.height

    for i in range(1, 8):
        print(f"===Day {i}===")
        rose.grow()
        rose.age()
        rose.show()

    total_growth: float = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()
