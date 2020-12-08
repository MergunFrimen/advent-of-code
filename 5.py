# --- Day 5: Binary Boarding ---


def highest_seat_id(filename: str) -> int:
    
    f = open(filename, 'r')
    max_seat_id = 0
    seat_ids = []

    for seat in f.read().split():
        seat_id = get_seat_id(seat)
        seat_ids.append(seat_id)

        if seat_id > max_seat_id:
            max_seat_id = seat_id

    seat_ids.sort()
    print("empty seat: ", find_empty_seat(seat_ids))

    return max_seat_id
        

def get_seat_id(seat: str) -> int:
    
    in_binary = '' 

    for x in seat:
        if x == 'F' or x == 'L':
            in_binary += '0'
        if x == 'B' or x == 'R':
            in_binary += '1'

    return (int(in_binary[:7], 2) * 8) + int(in_binary[7:], 2)


def find_empty_seat(seat_ids) -> int:

    for i in range(len(seat_ids) - 1):
        if seat_ids[i+1] != seat_ids[i] + 1:
            print(seat_ids[i], seat_ids[i+1])
            return seat_ids[i] + 1


print(highest_seat_id('input.txt'))
