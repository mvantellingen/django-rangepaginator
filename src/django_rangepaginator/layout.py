def calculate_pages(current, total, distance=2, edge=1):
    center = min(max(distance + 1, current), total - distance)
    add_skip_start = add_skip_end = False
    pages = set()

    # Add the page numbers on the start
    for i in range(1, edge + 1):
        pages.add(i)

    # Add range of the current page
    for i in range(max(1, center - distance), min(center + distance + 1, total)):
        pages.add(i)

    # Add page numbers on the end
    for i in range(total + 1 - edge, total + 1):
        pages.add(i)

    # Check if we need to insert a 'skip' or can just fill in the number. Do
    # this for both the start and the end
    if center - distance > edge:
        if edge + 2 in pages:
            pages.add(edge + 1)
        else:
            add_skip_start = True

    if center + distance < total - edge:
        if center + distance + 2 in pages:
            pages.add(center + distance + 1)
        else:
            add_skip_end = True

    pages = sorted(pages)

    # Insert the skip items
    if add_skip_start:
        pages.insert(edge, None)
    if add_skip_end:
        pages.insert(0 - edge, None)

    return pages
