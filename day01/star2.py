def process(lines: list[str]):
    lines = [[int(x) for x in line.split(' ') if x != ""] for line in lines]

    left = sorted([x[0] for x in lines])
    right = sorted([x[1] for x in lines])

    _sum = 0
    for item in left:
        _sum += item * len([1 for x in right if x == item])
    print(_sum)


def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    process(lines)


if __name__ == "__main__":
    main()
