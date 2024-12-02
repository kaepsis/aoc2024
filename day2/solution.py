file_data = open("data.txt", "r").readlines()

def is_safe(row):
    direction = None
    for i in range(len(row) - 1):
        diff = row[i + 1] - row[i]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if direction is None:
            direction = "up" if diff > 0 else "down"
        else:
            if (direction == "up" and diff < 0) or (direction == "down" and diff > 0):
                return False
    return True

def part1():
    safe_count = 0
    for row in file_data:
        row = row.replace("\n", "")
        row = [int(n) for n in row.split()]
        if is_safe(row):
            safe_count += 1
    return safe_count

def part2():
    safe_count = 0
    for row in file_data:
        row = row.replace("\n", "")
        row = [int(n) for n in row.split()]
        if is_safe(row):
            safe_count += 1
            continue
        for i in range(len(row)):
            modified_row = row[:i] + row[i + 1:]
            if is_safe(modified_row):
                safe_count += 1
                break
    return safe_count

print(part2())