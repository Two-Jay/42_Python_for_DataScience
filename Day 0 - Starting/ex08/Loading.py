def ft_tqdm(lst: range) -> None:
    """
    ft_tqdm(range) -> None

    print a progress bar with a percentage and a loading bar
    and yield the current element of the range
    """
    limit = lst.stop
    arrow_maximum_len = 100
    for elem in range(len(lst) + 1):
        current_progress = elem / limit * 100
        loading_progress = f"{elem}/{limit}"
        base = 100 / arrow_maximum_len
        arrow = "█" * int(current_progress / base)
        print(f"{current_progress:03.0f}%|{arrow:<{arrow_maximum_len}}| {loading_progress}", end="\r")
        yield elem

