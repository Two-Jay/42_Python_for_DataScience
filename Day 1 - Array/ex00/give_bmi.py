def validate_bmi_list(lst : list[int | float]) -> bool:
    """
    function to validate bmi list by conditions
    the conditions to check the parameter is error are :
        - the parameter is not list
        - the parameter : list is contain an element which is not int or float
    """
    try:
        if type(lst) is not list:
            raise ValueError("the arguments are bed.")
        if any(filter(lambda x : type(x) is int | float, lst)):
            raise ValueError("the arguments are bed.")
        return True
    except:
        return False

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    function works with two list
        - height list : list[int or float]
        - weight list : list[]
    it returns a list of bmi calculated by the parameters
    the fomular to use for calculation of BMI is :
        weight / height ^ 2 = bmi
    """
    if all([validate_bmi_list(height), validate_bmi_list(height)]) == False and \
        len(height) is not len(weight):
        return None
    return [w / h ** 2 for h, w in zip(height, weight)]

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if validate_bmi_list(bmi) == False:
        return None
    return [True if v > limit else False for v in bmi]