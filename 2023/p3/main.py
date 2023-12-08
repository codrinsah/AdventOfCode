import re   

def solve():
    with open("2023/p3/input.txt") as f:
        total = 0
        matrix: list[str] = []
        for line in f.readlines():
            matrix.append(line.strip())
        mapper: dict[tuple[int, int], list[int]] = {}
        for gear_line in range(len(matrix)):
            for gear_col in range(len(matrix[0])):
                mapper[(gear_line, gear_col)] = []
        for line_idx in range(len(matrix)):
            line = matrix[line_idx]
            col_idx = 0
            while col_idx < len(line):
                char = line[col_idx]
                if char.isdigit():
                    start = col_idx
                    end = col_idx
                    while end < len(line) and line[end].isdigit():
                        end += 1
                    end = end - 1
                    number = int(line[start:end+1])
                    for gear_line in range(line_idx - 1, line_idx + 2):
                        for gear_col in range(start - 1, end + 2):
                            if gear_line < 0 or gear_col < 0 or gear_line >= len(matrix) or gear_col >= len(line):
                                continue
                            if matrix[gear_line][gear_col] == '*':
                                mapper[(gear_line, gear_col)].append(number)
                    col_idx = end
                col_idx += 1
        for key, value in mapper.items():
            if len(value) == 2:
                total += value[0] * value[1]
        print(total)

solve()