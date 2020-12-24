#!/usr/bin/env python3

# --- Day 23: Crab Nodes ---

from typing import Optional, List


node_amount = 9
round_amount = 100


class Node:

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional['Node'] = None
    
    def __repr__(self) -> str:
        return f'Node(Label: {self.value}, Next: {self.next.value if self.next else None})'

    def __str__(self) -> str:
        result = ""
        for _ in range(round_amount - 1):
            result += f"{self.value} -> "
            self = self.next
        return result + 'None'



def read(filename: str) -> List[int]:
    with open(filename, 'r') as f:
        return [int(x) for x in f.read()[:-1]]


def solve_part2(data: List[int]) -> int:

    # Generate all nodes in list
    nodes = [Node(i) for i in range(node_amount + 1)]
    
    # Connect node to next node
    for i in range(len(data) - 1):
        nodes[data[i]].next = nodes[data[i + 1]]

    # Connect last node to first in next batch
    # nodes[data[-1]].next = nodes[len(data) + 1]

    # # Add rest of the nodes
    # for i in range(len(data) + 1, node_amount):
    #     nodes[i].next = nodes[i + 1]
    # # Loop back
    nodes[data[-1]].next = nodes[data[0]]

    print(nodes[1])
    
    # Main game loop
    current_node = nodes[data[0]]
    for i in range(round_amount):
        move(nodes, current_node)
        current_node = current_node.next
    
    return nodes[1].next.value * nodes[1].next.next.value


def move(nodes: List[Node], curr: Node) -> None:

    three_cups = [curr.next, curr.next.next, curr.next.next.next]
    curr.next = curr.next.next.next.next

    # Find the destination cup
    dest = curr.value - 1
    while dest in three_cups or dest == 0:
        dest -= 1
        if dest <= 0:
            dest = node_amount

    # Insert those three nodes
    three_cups[-1].next = nodes[dest].next
    nodes[dest].next = three_cups[0]


def main() -> None:
    data = read('input.txt')
    solution2 = solve_part2(data)
    print(f"--- Part Two ---\n{solution2}")


main()
