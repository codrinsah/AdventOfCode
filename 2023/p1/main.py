import re
import os

def convert_str_to_digit(text: str):
    match text:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return int(text)
        
with open("2023/p1/input.txt") as f:
    sum = 0
    for line in f.readlines():
        digit1 = convert_str_to_digit(re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line)[0])
        digit2 = convert_str_to_digit(re.findall(r"\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", line[::-1])[0][::-1])
        sum += digit1 * 10 + digit2
    print(sum)