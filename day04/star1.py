import re

def transpose(lines: list[str]):
    return [''.join(s) for s in zip(*lines)]


def process(lines: list[str]):
    score = 0
    xmas = re.compile(r'XMAS')
    samx = re.compile(r'SAMX')

    for line in lines:
        score += len(xmas.findall(line))
        score += len(samx.findall(line))

    cols = transpose(lines)
    for col in cols:
        score += len(xmas.findall(col))
        score += len(samx.findall(col))

    for i in range(len(lines)-3):
        for j in range(len(lines[0])-3):
            if all([lines[i+k][j+k] == c for k,c in enumerate('XMAS')]) or all([lines[i+k][j+k] == c for k,c in enumerate('SAMX')]):
                score += 1

    for i in range(3, len(lines)):
        for j in range(len(lines[0])-3):
            if all([lines[i-k][j+k] == c for k,c in enumerate('XMAS')]) or all([lines[i-k][j+k] == c for k,c in enumerate('SAMX')]):
                score += 1

    print(score)


def main():
    with open("./input.txt", "r") as f:
        lines = [line.replace('\n', '') for line in f.readlines()]

    process(lines)


if __name__ == "__main__":
    main()
