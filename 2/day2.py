"""
Invalid IDs.

Better ideas for part 2: directly generate repeated pattern
numbers within range. Use math (ABCABC = ABC * 1001).
"""

total1 = 0
total2 = 0

with open("input.txt") as f:
    lines = f.readlines()
    line = lines[0]

    for id_range in line.split(","):
        s, e = id_range.split("-")
        s, e = int(s), int(e)
        for i in range(s, e + 1, 1):
            i_str = str(i)
            n = len(i_str)

            for l in range(1, n // 2 + 1):
                if n % l == 0 and i_str == i_str[0:l] * (n // l):
                    # print(i)
                    total2 += i
                    break

            if n % 2 == 1:
                continue
            if i_str[0:n//2] == i_str[n//2:]:
                total1 += i

print(total1)
print(total2)
