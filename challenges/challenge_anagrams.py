def is_anagram(first_string, second_string):
    first_string = merge_sort_string(first_string.lower())
    second_string = merge_sort_string(second_string.lower())

    if not first_string or not second_string:
        return (first_string, second_string, False)

    return (first_string, second_string, first_string == second_string)


# Funções criadas a partir do código extraído do course da Trybe
def merge_sort_string(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = merge_sort_string(string[:mid])
    right = merge_sort_string(string[mid:])

    return merge_ordered(left, right, string)


def merge_ordered(left, right, string):
    merged = list(string)
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

    return "".join(merged)
