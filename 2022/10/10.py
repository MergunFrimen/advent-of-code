

class CPU:
    def __init__(self, instructions):
        self.x = 1
        self.instructions = instructions
        self.current_instruction = instructions.pop()
        self.instruction_cycles = 0
        self.done = False
    
    def cycle(self):
        if self.done:
            return
        self.instruction_cycles += 1
        if self.current_instruction is None and self.instruction_cycles == 1:
            self.new_instruction()
        elif self.current_instruction is not None and self.instruction_cycles == 2:
            self.x += self.current_instruction
            self.new_instruction()

    def new_instruction(self):
        if not self.instructions:
            self.done = True
            return
        self.current_instruction = self.instructions.pop()
        self.instruction_cycles = 0
    

def get_data():
    with open('input.txt') as f:
        return [(None if x == "noop" else int(x.split()[1])) for x in f.read().split('\n')[:-1]][::-1]


def part1(data):
    total = 0
    cpu = CPU(data)
    for i in range(1, 221):
        if i == 20 or (i - 20) % 40 == 0:
            total += cpu.x * i
        cpu.cycle()
    return total


def get_pixel(sprite_position, crt_position):
    if sprite_position - 1 <= crt_position <= sprite_position + 1:
        return '#'
    return '.'


def part2(data):
    screen = [['.'] * 40 for _ in range(6)]
    cpu = CPU(data)
    
    for i in range(6):
        for j in range(40):
            print(cpu.x)
            screen[i][j] = get_pixel(cpu.x, j)
            cpu.cycle()
    
    for row in screen:
        print(' '.join(row))


def main():
    print(f'part1: {part1(get_data())}')
    print(f'part2: {part2(get_data())}')

main()