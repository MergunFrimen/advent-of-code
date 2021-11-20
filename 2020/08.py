from copy import deepcopy


def parse(raw):
   
    code = []

    for line in raw.split('\n')[:-1]:
        op, arg = line.split()
        code.append([0, [op, arg]])

    return code


def execute_code(code):

    max_pointer = len(code) - 1
    accu = 0
    pointer = 0

    while "infinite loop":
        
        if pointer > max_pointer:
            return accu

        instruction = code[pointer]

        counter = instruction[0]
        op = instruction[1][0]
        arg = int(instruction[1][1])

        # LOOPING !
        if counter != 0:
            return None
        
        if op == "acc":
            accu += arg
            pointer += 1
            instruction[0] += 1

        elif op == "jmp":
            pointer += arg
            instruction[0] += 1

        elif op == "nop":
            pointer += 1
            instruction[0] += 1

        else:
            print("invalid op", op)


def change_code(code):

    for i, instruction in enumerate(code):

        # NOP to JMP
        if instruction[1][0] == "nop":
            copy = deepcopy(code)
            copy[i][1][0] = "jmp"

            accu = execute_code(copy)

            if accu is not None:
                return accu

        # JMP to NOP
        if instruction[1][0] == "jmp":
            copy = deepcopy(code)
            copy[i][1][0] = "nop"

            accu = execute_code(copy)

            if accu is not None:
                return accu

    return None


def main():
    with open("input.txt", 'r') as f:
        raw = f.read()

    code = parse(raw)
    accu = change_code(code)

    print(accu)


main()
