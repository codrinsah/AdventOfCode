import re   

def solve():
    with open("2023/p5/input.txt") as f:
        seeds = [int(seed) for seed in re.findall(r"(\d+)", f.readline())]
        intervals = []
        i = 0
        while i < len(seeds):
            intervals.append((seeds[i], seeds[i] + seeds[i+1]))
            i = i + 2
        f.readline()
        line = f.readline()
        while line:
            mapString = line
            line = f.readline()
            intervals_copy = []
            interval_remaining = [interval for interval in intervals]
            while line and line != '\n':
                [dest, src, rng] = [int(nr) for nr in re.findall(r"(\d+)", line)]
                intervals = []
                for interval in interval_remaining:
                    if interval[1] <= src:
                        intervals.append(interval)
                        continue
                    if interval[0] >= src + rng:
                        intervals.append(interval)
                        continue
                    left = max(interval[0], src)
                    right = min(interval[1], src + rng)
                    intervals_copy.append((dest + left - src, dest + right - src))
                    if interval[0] < left:
                        intervals.append((interval[0], left))
                    if interval[1] > right:
                        intervals.append((right, interval[1]))
                interval_remaining = intervals
                line = f.readline()
            if line == '\n':
                f.readline()
            intervals.extend(intervals_copy)
        print(min(intervals))
solve()