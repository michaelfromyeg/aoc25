def fresh(vals, ranges):
    count = 0
    for v in vals:
        for mn, mx in ranges:
            if mn <= v and v <= mx:
                count += 1
                break
    return count


def fresh2(ranges):
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    new_ranges = []

    current_range = sorted_ranges[0]
    for next_range in sorted_ranges[1:]:
        if next_range[0] <= current_range[1]:
            # combine
            new_range = (current_range[0], max(current_range[1], next_range[1]))
            current_range = new_range
        else:
            new_ranges.append(current_range)
            current_range = next_range
    new_ranges.append(current_range)

    c = 0
    for r in new_ranges:
        c += r[1] - r[0] + 1

    return c


def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

        ranges = []

        idx = 0
        while idx < len(lines) and lines[idx].strip() != "":
            mn, mx = lines[idx].strip().split("-")
            ranges.append((int(mn), int(mx)))

            idx += 1
        # print(ranges)

        vals = []
        for line in lines[idx + 1 :]:
            line = line.strip()
            if line == "":
                continue
            vl = int(line)
            vals.append(vl)
        # print(vals)

        count = fresh(vals, ranges)
        print(count)

        count2 = fresh2(ranges)
        print(count2)


main()
