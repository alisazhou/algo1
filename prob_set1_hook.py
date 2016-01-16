from count_inversion import sort_and_count

with open('IntegerArray.txt', 'rb') as f:
    numbers = [int(str.strip(line)) for line in f.readlines()]

print(numbers[:4])

result = sort_and_count(numbers)
print(len(result[0]))
print(result[1])


