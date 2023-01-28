from challenges.challenge_anagrams import merge_ordered


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge_ordered(left, right, array)


def find_duplicate(nums):
    sorted_nums = merge_sort(nums)

    for i in range(len(sorted_nums) - 1):
        if (
            not nums
            or not isinstance(sorted_nums[i], int)
            or sorted_nums[i] < 0
        ):
            return False

        if sorted_nums[i] == sorted_nums[i + 1]:
            return sorted_nums[i]

    return False
