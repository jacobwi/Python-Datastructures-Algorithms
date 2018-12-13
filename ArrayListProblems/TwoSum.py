# Array/List we are searching in
nums = [4, 5, 2, 5, 40, 20, 1, 6, 11]

# Adding two indices would result in the target below
target = 7


# Method for finding the first two indices that add up to the target
def find_two_sum():
    result_dict = {}
    for j, num in enumerate(nums):
        ans = target - num
        if ans in result_dict:
            return [result_dict[ans], j]
        else:
            result_dict[num] = j


# Method for finding the all sets of two indices that add up to the target
def find_all_two_sum():
    result_dict = []
    for i in range(len(nums)):
        for x in range(i + 1, len(nums)):
            if (nums[i] + nums[x]) == target:
                 result_dict.append([i, x])

    return result_dict


# Test
print(find_two_sum())
print(find_all_two_sum())
