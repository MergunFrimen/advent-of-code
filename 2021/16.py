from operator import mul
from functools import reduce

translate = {
             "0": "0000",
             "1": "0001",
             "2": "0010",
             "3": "0011",
             "4": "0100",
             "5": "0101",
             "6": "0110",
             "7": "0111",
             "8": "1000",
             "9": "1001",
             "A": "1010",
             "B": "1011",
             "C": "1100",
             "D": "1101",
             "E": "1110",
             "F": "1111"
            }

def get_header(m, i):
    return int(m[i:i+3], 2), int(m[i+3:i+6], 2)

def get_lengthtype(m, i):
    return int(m[i], 2)

def get_bitlength(m, i):
    return int(m[i:i+15], 2)

def get_packetamount(m, i):
    return int(m[i:i+11], 2)

def get_literal(m, i):
    literal = ""
    while True:
        literal += m[i+1:i+5]
        i += 5
        if m[i-5] == "0":
            break
    return int(literal, 2), i

def parse(m):
    packets = []
    i = 0

    while set(m[i:]) != {'0'} and i < len(m):
        # read header
        packet = [*get_header(m, i)]
        i += 6
        # packet is literal
        if packet[1] == 4:
            literal, i = get_literal(m, i)
            packet += [literal]
        # packet is an operator
        else:
            packet += [get_lengthtype(m, i)]
            i += 1
            if packet[2] == 0:
                packet += [get_bitlength(m, i)]
                i += 15
            else:
                packet += [get_packetamount(m, i)]
                i += 11
        # add length of each packet
        packet = [i - sum(p[0] for p in packets)] + packet
        packets += [packet]

    return packets

def operation(t, s):
    if t == 0:
        return sum(s)
    elif t == 1:
        # return product(s)
        return reduce(mul, s, 1)
    elif t == 2:
        return min(s)
    elif t == 3:
        return max(s)
    elif t == 5:
        return s[0] > s[1]
    elif t == 6:
        return s[0] < s[1]
    elif t == 7:
        return s[0] == s[1]
    assert False

def calculate(packets):
    p = packets.pop(0)
    read = p[0]
    s = []

    # literal packet
    if p[2] == 4:
        return p[3], read

    # operator packet
    if p[3] == 0:
        while read < p[0] + p[4]:
            v, l = calculate(packets)
            read += l
            s += [v]
    elif p[3] == 1:
        for _ in range(p[4]):
            v, l = calculate(packets)
            read += l
            s += [v]
    return operation(p[2], s), read

packets = parse(''.join([translate[x] for x in open("input/16.txt").read().rstrip()]))
print(sum(p[1] for p in packets))
print(calculate(packets)[0])
