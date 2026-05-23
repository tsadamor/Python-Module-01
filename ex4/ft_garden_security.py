class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height = 0.0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)

    def show(self) -> None:
        print(
            f"Current state: "
            f"{self.name}: {self._height}cm, {self._age} days old"
        )


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(
        f"Plant created: "
        f"{rose.name}: {rose.get_height()}cm, {rose.get_age()} days old"
    )
    print()

    rose.set_height(25.0)
    print(f"Height updated: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()}cm")
    print()

    rose.set_height(-15.0)
    rose.set_age(-10)
    print()

    rose.show()


if __name__ == "__main__":
    main()
