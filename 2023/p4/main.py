import re   

def solve():
    with open("2023/p4/input.txt") as f:
        total = 0
        lines = f.readlines()
        counts = [1 for _ in lines]
        for idx, line in enumerate(lines):
            cards = line.split(':')[1]
            [winning, player] = cards.split("|")
            winning = [int(x) for x in re.findall(r"\d+", winning)]
            player = [int(x) for x in re.findall(r"\d+", player)]
            cnt = 0
            for card in player:
                if card in winning:
                    cnt += 1
            for i in range(cnt):
                counts[idx + i + 1] += counts[idx]
        print(sum(counts))

solve()