def get_columns():
    SPACER = "   "
    file_data = open("data.txt", "r").readlines()
    left_column = []
    right_column = []
    for line in file_data:
        line = line.replace("\n", "")
        numeri = line.split(SPACER)
        left, right = int(numeri[0]), int(numeri[1])
        left_column.append(left)
        right_column.append(right)
    return left_column, right_column

left_column, right_column = get_columns()

# Part 1
left_column_sorted = sorted(left_column)
right_column_sorted = sorted(right_column)
distances = []
for left, right in zip(left_column_sorted, right_column_sorted):
    if left < right:
        distances.append(right-left)
    else:
        distances.append(left-right)

# Part 2
similarity_scores = []
for number in left_column:
    occurrencies = right_column.count(number)
    similarity_scores.append(number * occurrencies)

print(f"Part 1 solution: {sum(distances)}")
print(f"Part 2 solution: {sum(similarity_scores)}")