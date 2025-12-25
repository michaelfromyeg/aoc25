from functools import reduce


def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

        parts = []
        for line in lines[:-1]:
            line = line.strip()
            ps = line.split()
            parts.append([int(part) for part in ps])
        print(parts)

        ops = lines[-1].strip().split()
        print(ops)

        parts = [list(row) for row in zip(*parts)]

        total = 0
        for i, part in enumerate(parts):
            if ops[i] == "+":
                total += sum(part)
            else:
                total += reduce(lambda x, y: x * y, part)
        print(total)


main()
