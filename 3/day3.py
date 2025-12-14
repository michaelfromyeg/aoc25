"""
Joltage.

Turns out: actually faster to remove digits?
"""

total1 = 0
total2 = 0

def next_digit(line, imin, imax):
    idx, digit = imin, int(line[imin])
    for i, c in enumerate(line[0:imax]):
        if i <= imin:
            continue
        if int(c) > digit:
            idx, digit = i, int(c)
    return idx, digit

with open("input.txt") as f:
    # print("01234567890123456789")

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue

        n = len(line)

        # tens_index, tens_digit = 0, int(line[0])
        # for index, c in enumerate(line[0:len(line)-1]):
        #     if index == 0:
        #         continue
        #     if int(c) > tens_digit:
        #         tens_index, tens_digit = index, int(c)
        tens_index, tens_digit = next_digit(line, 0, n-1)


        # ones_index, ones_digit = tens_index + 1, int(line[tens_index + 1])
        # for index, c in enumerate(line):
        #     if index <= tens_index:
        #         continue
        #     if int(c) > ones_digit:
        #         ones_index, ones_digit = index, int(c)
        ones_index, ones_digit = next_digit(line, tens_index + 1, n)
        
        if ones_index < tens_index:
            raise Exception("Invalid indices")
        total1 += tens_digit * 10 + ones_digit

        # part 2
        digits = []
        k = 12

        if n < k:
            raise Exception("Line too short")

        imin, imax = 0, n - (k-1)

        for i in range(k):
            ni, nd = next_digit(line, imin, imax)
            digits.append(nd)
            imin = ni + 1
            imax += 1
        
        for i, digit in enumerate(digits):
            total2 += digit * (10 ** (k - i - 1))

print(total1)
print(total2)
