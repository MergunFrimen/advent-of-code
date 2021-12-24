trans = {
         "0" : "0000",
         "1" : "0001",
         "2" : "0010",
         "3" : "0011",
         "4" : "0100",
         "5" : "0101",
         "6" : "0110",
         "7" : "0111",
         "8" : "1000",
         "9" : "1001",
         "A" : "1010",
         "B" : "1011",
         "C" : "1100",
         "D" : "1101",
         "E" : "1110",
         "F" : "1111"
         }

def get_header(m):
    return int(m[0:3], 2), int(m[3:6], 2)

def get_length(m):
    if m[0] == 0:
        return 0, int(m[1:16], 2)
    return 1, int(m[1:12], 2)

def get_value(m):
    n = ""
    for i in range(len(m), 5):
        n += m[i+1:i+5]
        if m[i] == 0:
            break
    return int(n, 2)

def read():
    return open("input/16.txt").read().rstrip()

def hex2bin(m):
    return ''.join(trans[x] for x in m)

def part1():
    m = hex2bin(read())
    rec(m, 0)

def part2():
    m = read()

part1()
part2()
