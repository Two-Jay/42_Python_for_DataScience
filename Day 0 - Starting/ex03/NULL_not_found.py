def NULL_not_found(object : any) -> int:
    checked = type(object)
    if object == None:
        print(f"Nothing : {object} {checked}")
    elif type(object) == float and object != object:
        print(f"cheese : {object} {checked}")
    elif type(object) == int and object == 0:
        print(f"Zero : {object} {checked}")
    elif type(object) == str and object == '':
        print(f"Empty : {object} {checked}")
    elif type(object) == bool and object == False:
        print(f"Fake : {object} {checked}")
    else:
        print("Type not found")
        return 1