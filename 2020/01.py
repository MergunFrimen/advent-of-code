def get_nums(filename: str) -> None:

    f = open(filename, 'r')
    nums = [int(x) for x in f.read().split('\n') if x.isdecimal()]
    nums.sort()
    
    for x in nums:
        for y in nums[1:]:
            for z in nums[2:]:
                if x + y + z == 2020:
                    return x*y*z
    
    f.close()


print(get_nums('input.txt'))
