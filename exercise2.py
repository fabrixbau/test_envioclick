def sort_by_priority(data, criteria):
    matching_items = []
    non_matching_items = []

    for item in data:
        if matches_criteria(item, criteria):
            matching_items.append(item)
        else:
            non_matching_items.append(item)

    sorted_matching_items = manual_sort_by_priority(matching_items)

    return sorted_matching_items + non_matching_items


# This block is used to count how many elements there are in the items
# list, without using the native len() function.
def matches_criteria(item, criteria):
    for field, operator, value in criteria:
        item_value = item[field]

        if operator == '=' and item_value != value:
            return False
        elif operator == '>' and item_value <= value:
            return False
        elif operator == '<' and item_value >= value:
            return False
        elif operator == '>=' and item_value < value:
            return False
        elif operator == '<=' and item_value > value:
            return False
        elif operator == '!=' and item_value == value:
            return False

    return True


# ordern by bubble sort classic
def manual_sort_by_priority(filtered):
    n = len(filtered)
    for i in range(n):
        for j in range(0, n - i - 1):
            if filtered[j]["priority"] < filtered[j + 1]["priority"]:
                filtered[j], filtered[j + 1] = filtered[j + 1], filtered[j]
    return filtered
