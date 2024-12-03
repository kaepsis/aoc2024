import re
import math

file_data = open("data.txt", "r").read()

def part1():
    pattern = r"mul\([0-9]+,[0-9]+\)"
    groups = re.findall(pattern, file_data)
    results = []
    for group in groups:
        inner_pattern = r"[0-9]+"
        inner_groups = [int(inner_group) for inner_group in re.findall(inner_pattern, group)]
        results.append(math.prod(inner_groups))
    print(sum(results))

def part2():
    pattern = r"mul\([0-9]+,[0-9]+\)|(don't\(\)|do\(\))"
    found_groups = re.finditer(pattern, file_data)
    groups = [match.group() for _, match in enumerate(found_groups)]
    accepted_groups = []
    mul_enabled = True
    for group in groups:
        if group == "do()":
            mul_enabled = True
        elif group == "don't()":
            mul_enabled = False
        elif group.startswith("mul("):
            if mul_enabled:
                accepted_groups.append(group)
    results = []
    for group in accepted_groups:
        inner_pattern = r"[0-9]+"
        inner_groups = [int(inner_group) for inner_group in re.findall(inner_pattern, group)]
        results.append(math.prod(inner_groups))        
    print(sum(results))