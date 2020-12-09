

# --- Day 9: Encoding Error ---


def is_sum_of_two(n, nums):

    # Probably not the best way to do this
    # but hey it works

    for x in nums:
        for y in nums[1:]:
            if n == x + y:
                return True

    return False


def find_invalid(nums, wnd_size):

    for i in range(len(nums) - wnd_size):
        if not is_sum_of_two(nums[i + wnd_size], nums[i:i + wnd_size]):
            return nums[i + wnd_size]


def find_sum(nums, invalid):

    for i in range(len(nums) - 1):
        s = nums[i]

        for x in range(i + 1, len(nums)):
            s += nums[x]

            if s > invalid:
                break
            if s == invalid:
                return (i, x)


def main():

    with open('input.txt', 'r') as f:
        raw = f.read()

    nums = [int(x) for x in raw.split('\n')[:-1]]

    invalid_num = find_invalid(nums, 25)
    x, y = find_sum(nums, invalid_num)

    print("--- Part One ---\n", invalid_num)
    print("--- Part Two ---\n", min(nums[x:y+1]) + max(nums[x:y+1]))


main()
