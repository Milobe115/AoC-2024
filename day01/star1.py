def process(lines: list[str]):
    lines = [[int(x) for x in line.split(' ') if x != ""] for line in lines]

    left = sorted([x[0] for x in lines])
    right = sorted([x[1] for x in lines])

    sum = 0
    for idx in range(len(left)):
        sum += abs(left[idx] - right[idx])
    print(sum)


def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    process(lines)


if __name__ == "__main__":
    main()
