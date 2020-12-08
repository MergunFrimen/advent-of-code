with open('input.txt', 'r') as f:
    counter = 0
    for x in f.read().split('\n\n'):
        group = set(x.split('\n')[0])

        for y in x.split('\n')[1:]:
            if y == '':
                continue
            group &= set(y)
        counter += len(group)
        print(x.split('\n'))
        print(group, len(group))
    print(counter)



