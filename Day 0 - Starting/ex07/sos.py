import argparse as ap
import sys

sys.tracebacklimit = 0


def validate_string_by_morse(string: str, morse_dict) -> None:
    keys = morse_dict.keys()
    for char in string:
        assert char.upper() in keys, "the argument is bad"


def convert_to_morse(string: str) -> str:
    """
    function to convert a string to morse code
    """
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': '/'
    }
    validate_string_by_morse(string, NESTED_MORSE)
    return ' '.join(map(lambda char: NESTED_MORSE[char.upper()], string))


def get_args() -> ap.Namespace:
    parser = ap.ArgumentParser()
    parser.add_argument("arg", type=str, nargs='*')
    length = len(parser.parse_args().arg)
    assert length == 1, "the argument is bad"
    assert str(parser.parse_args().arg[0]), "the argument is bad"
    return parser.parse_args().arg[0]


def main(args: str) -> None:
    print(convert_to_morse(args))


if __name__ == "__main__":
    main(get_args())
