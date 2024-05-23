def sort_list(lst):

    sr_ar = sum(lst) / len(lst)

    sort_length = int(len(lst) * 2 / 3) if sr_ar > 0 else int(len(lst) / 3)

    sorted_part = sorted(lst[:sort_length])

    reversed_part = lst[sort_length:][::-1]

    return sorted_part + reversed_part

list = [10, 5, 2, 19, 8, 1, 7, 11, 3, 6, 4, 9]
print(sort_list(list))
