#!/usr/bin/env python3


# --- Day 18: Operation Order ---


# 1 + (2 * 3) + (4 * (5 + 6))
#        6      (4 *    11  )
#                    44

# 1 +    6    +      44


def solve(data):

    result = []
    queue = []
    o_bracket = 0
    i = 0

    while i < len(data):

        if o_bracket == 0:
            print(data[i])

        if data[i] == '(':
            o_bracket += 1
        if o_bracket:
            queue.append(data[i])
        if data[i] == ')':
            o_bracket -= 1

        i += 1

    print("".join(queue))
    return "".join(queue)


test = "1 + (2 * 3) + (4 * (5 + 6))"
data = test.replace(' ', '')
data = solve(data)
data = solve(data)
