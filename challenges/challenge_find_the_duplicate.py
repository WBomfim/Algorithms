def merge(left, right, merged):
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            merged[left_index + right_index] = left[left_index]
            left_index += 1
        else:
            merged[left_index + right_index] = right[right_index]
            right_index += 1

    for left_index in range(left_index, len(left)):
        merged[left_index + right_index] = left[left_index]

    for right_index in range(right_index, len(right)):
        merged[left_index + right_index] = right[right_index]

    return merged


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array)


def find_duplicate(nums):
    if not nums or not isinstance(nums[0], int) or nums[0] < 0:
        return False

    sorted_nums = merge_sort(nums)

    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i] == sorted_nums[i + 1]:
            return sorted_nums[i]

    return False
