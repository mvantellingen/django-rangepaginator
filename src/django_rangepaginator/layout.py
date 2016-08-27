def calculate_pages(current, total, distance=2):
    lower_bound = max(1, current - distance)
    upper_bound = min(total, current + distance)

    items = []
    if lower_bound > 1:
        items.append(1)

    if lower_bound > 3:
        items.append(None)
    elif lower_bound > 2:
        items.append(2)

    for item in range(lower_bound, upper_bound + 1):
        items.append(item)

    if upper_bound + 2 < total:
        items.append(None)
    elif upper_bound + 1 < total:
        items.append(total - 1)

    if upper_bound < total:
        items.append(total)

    return items
