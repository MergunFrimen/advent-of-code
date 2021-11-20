#!/usr/bin/env python3

from typing import Tuple, List
import re

# --- Day 16: Ticket Translation ---


class TicketInfo:
    def __init__(self, name: str, r1: Tuple[int, int],
                 r2: Tuple[int, int]) -> None:
        self.name = name
        self.range1 = range(r1[0], r1[1] + 1)
        self.range2 = range(r2[0], r2[1] + 1)
        self.values = []

    def add_value(self, value: int) -> None:
        self.values.append(value)

    def remove_value(self, value: int) -> None:
        if value in self.values:
            self.values.remove(value)


def read(filename: str) -> Tuple[List[TicketInfo], List[int], List[List[int]]]:
    with open(filename, 'r') as f:
        raw = f.read()[:-1]

    # Divide into categories
    ticket_data, my_ticket, other_tickets = raw.split('\n\n')

    # Parse my_ticket and other_tickets
    my_ticket = [int(x) for x in my_ticket.split('\n')[1].split(',')]
    other_tickets = [[int(y) for y in x.split(',')] for x in other_tickets.split('\n')[1:]]

    # Parse ticket_data and append tickets with set names and ranges
    ticket_data_regex = r"([a-z ]*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)"
    ticket_data = [re.findall(ticket_data_regex, row)[0] for row in ticket_data.split('\n')]
    ticket_info_list = []
    for name, r11, r12, r21, r22 in ticket_data: 
        ticket_info_list.append(TicketInfo(name, (int(r11), int(r12)), (int(r21), int(r22))))

    return (ticket_info_list, my_ticket, other_tickets)


def solve_part1(data):
    # Go through each ticket and check if its fields fall into any ticket_info range.
    # Return sum of all ticket fields that don't fall into any range (error rate).

    ticket_info_list, _, other_tickets = data
    error_rate = 0

    for ticket in other_tickets:
        for field in ticket:
            if not validate_range(ticket_info_list, field):
                error_rate += field

    return error_rate


def solve_part2(data):
    # Map all valid columns to ticket info types
    # Then just start adding one column to each ticket
    
    ticket_info_list, my_ticket, other_tickets = data
    other_tickets += [my_ticket]
    name_column_mapping = {}
    result = 1
    i = 0
    
    # Filter out invalid tickets
    for ticket in other_tickets[:]:
        for field in ticket:
            if not validate_range(ticket_info_list, field):
                other_tickets.remove(ticket)
                break

    # Adds column values to ticket_infos
    for ticket_info in ticket_info_list:
        add_values(ticket_info, other_tickets)

    # Find unique column for each ticket info
    while ticket_info_list:
        ticket_info = ticket_info_list[i % len(ticket_info_list)]
        value = ticket_info.values[0]

        if len(ticket_info.values) == 1:
            remove_values(ticket_info_list, value) 
            name_column_mapping[ticket_info.name] = value
            ticket_info_list.remove(ticket_info)

        i += 1

    # Calculate departure fields of my_ticket
    for name, value in name_column_mapping.items():
        if re.search("departure", name):
            result *= my_ticket[value]

    return result 


def add_values(ticket_info, other_tickets):
    for col in range(len(other_tickets[0])):
        valid = True
        for row in other_tickets:
            if row[col] not in ticket_info.range1 and row[col] not in ticket_info.range2:
                valid = False
                break
        if valid:
            ticket_info.add_value(col)


def remove_values(ticket_info_list, value):
    for ticket_info in ticket_info_list:
        if value in ticket_info.values:
            ticket_info.remove_value(value)

 
def validate_range(ticket_info_list, field):
    for ticket_info in ticket_info_list: 
        if field in ticket_info.range1 or field in ticket_info.range2:
            return True
    return False


def main() -> None:
    data = read('input.txt')
    solution1 = solve_part1(data)
    solution2 = solve_part2(data)
    print("--- Part One ---\n", solution1)
    print("--- Part Two ---\n", solution2)


main()
