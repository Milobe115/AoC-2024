def process(lines: list[str]):
    score = 0
    patterns = ['MMSS', 'SMMS', 'SSMM', 'MSSM']

    for i in range(len(lines)-2):
        for j in range(len(lines[0])-2):
            key = lines[i][j] + lines[i][j+2] + lines[i+2][j+2] + lines[i+2][j]
            if key in patterns and lines[i+1][j+1] == 'A':
                score += 1

    print(score)


def main():
    with open("./input.txt", "r") as f:
        lines = [line.replace('\n', '') for line in f.readlines()]

    process(lines)


if __name__ == "__main__":
    main()
