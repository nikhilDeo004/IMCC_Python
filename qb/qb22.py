nums = [5, 3, 9, 1]
nums.append(7)                       # (a) [5, 3, 9, 1, 7]
nums.insert(0, 0)                    # (b) [0, 5, 3, 9, 1, 7]
nums.remove(9)                       # (c) [0, 5, 3, 1, 7]
del nums[2]                          # (d) [0, 5, 1, 7]
print(sorted(nums, reverse=True))    # (e) [7, 5, 1, 0]
print(nums.index(min(nums)))         # (f) 0