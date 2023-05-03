def ft_filter(function_to_apply, list_of_inputs):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    return [i for i in list_of_inputs if function_to_apply(i) is True]
