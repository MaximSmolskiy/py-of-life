import random
import os
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Grid:
    height: int
    width: int
    grid: list[list[bool]] = field(default_factory=list)

    def init_random(self) -> None:
        assert self.height > 0 and self.width > 0

        self.grid = []
        for i in range(self.height):
            self.grid.append([])
            for _ in range(self.width):
                self.grid[i].append(bool(random.getrandbits(1)))

    def print_grid(self) -> None:
        print(" " + "＿" * (self.width + 1))

        for i in range(self.height):
            print("|", end=" ")

            for j in range(self.width):
                cell = "*" if self.grid[i][j] else " "
                print(cell, end=" ")

            print("|")

        print(" " + "＿" * (self.width + 1))


def clear_screen() -> None:
    """
    Determines and runs the correct system command in order to
    clear the screen.
    """

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main() -> None:
    raise NotImplementedError()


if __name__ == "__main__":
    main()
