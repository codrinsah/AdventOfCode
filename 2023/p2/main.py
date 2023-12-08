import re
        
max_red = 12
max_green = 13
max_blue = 14

def get_game_number_or_zero(line: str):
    match = re.split(r"Game (\d+): ", line)
    game_no = int(match[1])
    sessions = match[2].split(";")
    for session in sessions:
        session = session.strip()
        match = re.findall(r"(\d+) (blue|red|green)", session)
        for count_color in match:
            count = int(count_color[0])
            colour = count_color[1]
            match colour:
                case "red":
                    if count > max_red:
                        return 0
                case "green":
                    if count > max_green:
                        return 0
                case "blue":
                    if count > max_blue:
                        return 0
    return game_no

def get_game_power(line: str):
    min_red = 0
    min_green = 0
    min_blue = 0
    match = re.split(r"Game (\d+): ", line)
    game_no = int(match[1])
    sessions = match[2].split(";")
    for session in sessions:
        session = session.strip()
        match = re.findall(r"(\d+) (blue|red|green)", session)
        for count_color in match:
            count = int(count_color[0])
            colour = count_color[1]
            match colour:
                case "red":
                    min_red = max(min_red, count)
                case "green":
                    min_green = max(min_green, count)
                case "blue":
                    min_blue = max(min_blue, count)
    return min_red * min_green * min_blue

def solve():
    with open("2023/p2/input.txt") as f:
        total = 0
        for line in f.readlines():
            total += get_game_power(line)
        print(total)