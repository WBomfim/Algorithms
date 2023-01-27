def find_duplicate(nums):
    if not nums or len(nums) == 1:
        return False

    for i in range(len(nums)):
        if isinstance(nums[i], str) or nums[i] < 0:
            return False

        if count_duplicate(nums, nums[i]) > 1:
            return nums[i]

    return False


def count_duplicate(nums, num):
    count = 0

    for i in range(len(nums)):
        if nums[i] == num:
            count += 1

    return count
