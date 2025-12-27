"""
Pressing buttons.

Imagine you press the same button twice: what happens? (It undoes itself.)
So in the solution, each button is pressed once or not at all.

We have k buttons, so 2^k possible options.

Scrolling `input.txt`, `k` is quite smalll, so we can search it.

"""

from dataclasses import dataclass
from itertools import combinations

# from pprint import pprint
from shared import read_input

DEBUG = False

type Button = list[int]


@dataclass
class Machine:
    target: list[int]
    buttons: list[Button]
    joltage: list[int]


def parse_input(lines: list[str]) -> list[Machine]:
    """Parse input into structured data."""
    machines: list[Machine] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        values = line.split(" ")

        target_str = values[0]
        button_strs = values[1:-1]
        joltage_str = values[-1]

        target: list[int] = []
        for char in target_str[1:-1]:
            if char == ".":
                target.append(0)
            else:
                target.append(1)
        n = len(target)

        buttons = []
        for button_str in button_strs:
            vals = button_str[1:-1].split(",")
            button = [int(v) for v in vals]
            for b in button:
                assert b < n
            buttons.append(button)

        joltages = joltage_str[1:-1].split(",")
        joltage = [int(j) for j in joltages]

        machines.append(Machine(target, buttons, joltage))
    # pprint(machines)
    return machines


def get_minimum_presses(machine: Machine) -> int:
    # print(f"target: {machine.target}, buttons: {machine.buttons}")
    for r in range(len(machine.buttons) + 1):
        for subset in combinations(machine.buttons, r):
            start = [0] * len(machine.target)
            for button in subset:
                for b in button:
                    start[b] = 0 if start[b] == 1 else 1
            if start == machine.target:
                return r
    return -1


def part1(data: list[Machine]) -> int:
    """Solve part 1 of the puzzle."""
    presses = []
    for machine in data:
        press = get_minimum_presses(machine)
        if press == -1:
            raise ValueError("asdf")
        presses.append(press)
    return sum(presses)


def part2(data) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement part 2
    return 0


def main():
    lines = read_input(DEBUG)
    data = parse_input(lines)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
