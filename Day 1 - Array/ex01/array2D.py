import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
    function to slice 2D array.
    it slice the parametered 2d array by axies
    if an error occurs by conditions below , the function returns None
        - the parametered list is not list and not 2d array
        - the index 'start' and 'end' is out of range
    """
    def validate_family(family: list) -> bool:
        if type(family) == list:
            if all(type(i) == list for i in family):
                return True
        raise ValueError
        
    def validate_index(start: int, end: int, shape: tuple) -> bool:
        if all([type(start) == int, type(end) == int]):
            return True
        raise ValueError

    try:
        validate_family(family)
        target = np.array(family)
        validate_index(start, end, target.shape)
        sliced = target[start: end]
        print(f"My shape is : {target.shape}")
        print(f"My new shape is : {sliced.shape}")
        return sliced.tolist()
    except:
        return None