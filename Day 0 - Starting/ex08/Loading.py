def ft_tqdm(lst: range) -> None:
    """
    ft_tqdm(range) -> None

    print a progress bar with a percentage and a loading bar
    and yield the current element of the range
    """
    limit = lst.stop
    bar_width = 100
    for elem in range(len(lst) + 1):
        percent = elem / limit * 100
        load_count = f"{elem}/{limit}"
        base = 100 / bar_width
        arrow = "█" * int(percent / base)
        print(f"{percent:03.0f}%|{arrow:<{bar_width}}| {load_count}", end="\r")
        yield elem
