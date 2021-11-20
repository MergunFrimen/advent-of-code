

def traverse_slope(filename: str) -> int:
    
    f = open(filename, 'r')
    slope = f.read().split('\n')[:-1]

    slope0 = [x for x in slope] 
    slope1 = [x for x in slope] 
    slope2 = [x for x in slope] 
    slope3 = [x for x in slope] 
    slope4 = [x for x in slope] 

    counter = [0 for _ in range(5)]
    values  = [0 for _ in range(5)]
    
    for i, row in enumerate(slope):

        if i != 0 and i % 1 == 0:
            values[0] += 1
            values[1] += 3
            values[2] += 5
            values[3] += 7

            counter[0] += check(row, values[0])
            counter[1] += check(row, values[1])
            counter[2] += check(row, values[2])
            counter[3] += check(row, values[3])

        if i != 0 and i % 2 == 0:
            values[4] += 1
            counter[4] += check(row, values[4])

    f.close()
    return (
            counter[0] *
            counter[1] *
            counter[2] *
            counter[3] *
            counter[4]
            )


def check(row, value) -> int:

    right = value % len(row)

    if row[right] == '#':
        return 1

    if row[right] == '.':
        return 0


print(traverse_slope('input.txt'))
