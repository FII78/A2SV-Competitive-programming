nums = list(map(int,input().split()))
turtle = 0
hare = 0
for hare in range(len(nums)):
    if nums[hare] != 0 and nums[turtle] == 0:
        nums[turtle], nums[hare] = nums[hare], nums[turtle]
    if nums[turtle] != 0:
        turtle += 1
print(nums)

