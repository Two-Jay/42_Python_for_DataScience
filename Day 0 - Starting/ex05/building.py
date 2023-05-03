import argparse as ap
import sys

sys.tracebacklimit = 0

def dedent(string: str) -> str:
    """
    function to dedent a string
    """
    return string.replace('    ', '').replace('\t', '')

def check_string_by_conditions(string: str) -> None:
    """
    function to check a string by conditions
    """
    punctuations = [
        '?', '!', '.', ',', ';', ':', '(', ')',
        '[', ']', '{', '}', '"', "'", '-', '_'
    ]
    results = [
        len(string),
        len(''.join(filter(lambda char: char.isupper(), string))),
        len(''.join(filter(lambda char: char.islower(), string))),
        len(''.join(filter(lambda char: char in punctuations, string))),
        len(''.join(filter(lambda char: char.isspace(), string))),
        len(''.join(filter(lambda char: char.isdigit(), string)))
    ]
    return dedent(f"""\
            The text contains {results[0]} characters:
            - {results[1]} upper letters
            - {results[2]} lower letters
            - {results[3]} punctuations
            - {results[4]} spaces
            - {results[5]} digits\
        """)


def validate_args(args: list[str]) -> None:
    """
    function to validate arguments which are provided by the user
    the function will raise an error if:
    - no argument are provided
    - more than one argument are provideds
    """


def get_args():
    """
    function to get an argument which are provided by the user
    this function will return the first argument
    this function validate the arguments using validate_args()
    """
    parser = ap.ArgumentParser()
    parser.add_argument("arg", type=str, nargs='*')
    length = len(parser.parse_args().arg)
    if length == 0:
        return input("What is the text to count?\n")
    assert length <= 1, "more than one argument are provided"
    return parser.parse_args().arg[0]


def main(arg: str) -> None:
    """
    Main function
    """
    print(check_string_by_conditions(arg))


if __name__ == "__main__":
    main(get_args())
