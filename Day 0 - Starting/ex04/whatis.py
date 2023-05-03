import argparse as ap
import sys

sys.tracebacklimit = 0


def get_args() -> ap.Namespace:
    parser = ap.ArgumentParser()
    parser.add_argument("arg", type=str, nargs='*')
    length = len(parser.parse_args().arg)
    if length == 0:
        return None
    assert length <= 1, "more than one argument are provided"
    assert parser.parse_args().arg[0].lstrip('-').isdigit(), "argument is not an integer"
    return int(parser.parse_args().arg[0])

def iseven(number : int) -> bool:
    return number % 2 == 0

def print_iseven(number : int) -> None:
    print(f"I'm {'Even' if iseven(number) else 'Odd'}")

if __name__ == "__main__":
    target = get_args()
    if target != None:
        print_iseven(target)