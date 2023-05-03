import ft_filter as ftf
import argparse as ap
import sys

sys.tracebacklimit = 0


def validate_punctuations(string: str) -> bool:
    """
    function to validate if the string has a punctuation word
    """
    punctuations = [
        '?', '!', '.', ',', ';', ':', '(', ')',
        '[', ']', '{', '}', '"', "'", '-', '_'
    ]
    return any([True for char in string if char in punctuations])


def validate_args(args: list[str]) -> list[str]:
    """
    function to validate arguments which are provided by the user
    the function will raise an error if:
    - count of arguments is not 2
    - 1st argument is not a string
    - 2nd argument is not an integer
    """
    length = len(args)
    assert length == 2, "the arguments are bad"
    assert str(args[0]), "the first argument is not a string"
    assert not validate_punctuations(args[0]), "the arguments are bad"
    assert int(args[1]), "the second argument is not an integer"
    return args


def get_args() -> ap.Namespace:
    parser = ap.ArgumentParser()
    parser.add_argument("arg", type=str, nargs='*')
    checked = validate_args(parser.parse_args().arg)
    return checked


def main(args: list) -> None:
    """
    function to print a string with a number of times
    """
    splitted = args[0].split()
    base = int(args[1])
    print(ftf.ft_filter(lambda word: len(word) > base, splitted))


if __name__ == "__main__":
    main(get_args())
