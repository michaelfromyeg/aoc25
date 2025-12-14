"""
Turning a dial.

Tried doing divmod stuff but it didn't work.
"""

dial = 50
password1, password2 = 0, 0

with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        dir, amt = line[0], int(line[1:])

        while amt > 0:
            dial += 1 * (-1 if dir == 'L' else 1)
            dial %= 100

            amt -= 1

            if dial == 0:
                password2 += 1
        if dial == 0:
            password1 += 1

print(password1, password2)

