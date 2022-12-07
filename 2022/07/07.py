import re


def get_data():
    with open('input.txt') as f:
        return re.findall('\$ \w+ *\S*|dir \w+|\d+ \S+', f.read())


def create_metadata(data):
    cwd = ''
    metadata = {}
    ls = False
    for line in data[1:]:
        if line[0] == '$' and line[2:4] == 'cd':
            _, _, dirname = line.split()
            if dirname == '..':
                cwd = '/'.join(cwd.split('/')[:-1])
            else:
                cwd += '/' + dirname
            ls = False
        if line[0] == '$' and line[2:4] == 'ls':
            ls = True
            continue
        if ls:
            info, name = line.split()
            path = cwd + '/' + name
            metadata[path] = info
    return metadata


def get_dir_sizes(data):
    metadata = create_metadata(data)
    dir_sizes = dict([('/', 0)] + [(path, 0) for path, info in metadata.items() if info == 'dir'])
    
    for filepath, size in metadata.items():
        if size == 'dir':
            continue
        size = int(size)
        dir_sizes['/'] += size
        for i in range(1, filepath.count('/')):
            dirname = '/'.join(filepath.split('/')[:-i])
            dir_sizes[dirname] += size
    
    return dir_sizes


def part1(data):
    dir_sizes = get_dir_sizes(data)
    return sum(filter(lambda x: int(x) <= 10**5, dir_sizes.values()))


def part2(data):
    dir_sizes = get_dir_sizes(data)
    needed = 30000000 - (70000000 - dir_sizes['/'])
    return sorted(filter(lambda x: int(x) >= needed, dir_sizes.values()))[0]


def main():
    data = get_data()
    print(f'part1: {part1(data)}')
    print(f'part2: {part2(data)}')

main()