from copy import deepcopy


def is_sum(n, nums):

    for x in nums:
        for y in nums[1:]:
            if n == x + y:
                return True

    return False


def find_invalid(nums, wnd_size):

    # Checks if each number is a sum of some numbers in window
    # Returns first number that isn't a sum

    for i in range(len(nums) - wnd_size):
        if not is_sum(nums[i + wnd_size], nums[i:i + wnd_size]):
            return nums[i + wnd_size]


def find_sum(nums, invalid):

    for i in range(len(nums) - 1):
        accu = nums[i]

        for x in range(i+1, len(nums)):
            accu += nums[x]

            if accu > invalid:
                break
            
            if accu == invalid:
                return (i, x)


def parse(raw):

    return [int(x) for x in raw.split('\n')[:-1]]


def main():

    with open('input.txt', 'r') as f:
        raw = f.read()

    nums = parse(raw)

    wnd_size = 25
    invalid_num = find_invalid(nums, wnd_size)
    x, y = find_sum(nums, invalid_num)
    
    min_value = min(nums[x:y+1])
    max_value = max(nums[x:y+1])

    print(min_value + max_value)


main()
