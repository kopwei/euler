def get_sum_by_route(route_val, nums):
    sum_val = nums[0][0]
    j = 0
    route=[sum_val]
    for i in range(1, len(nums)):
        if route_val % 2 > 0:
            j+=1
        sum_val += nums[i][j]
        route.append(nums[i][j])
        route_val >>= 1
    return route, sum_val
            

s = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


lines = s.splitlines()
nums = []
for line in lines:
    line_list = [int(i) for i in line.split(' ')]
    nums.append(line_list)

possible_route = 2 ** (len(nums) - 1)
print("Possible routs: ", possible_route)

max_sum = 0
for i in range(possible_route):
    route, sum_val = get_sum_by_route(i, nums)
    if sum_val > max_sum:
        print("Max route updated", i)
        print("Route: ", route)
        max_sum = sum_val
print(max_sum)