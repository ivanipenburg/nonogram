import argparse
import os

from blocks import Blocks
from display_game import display_game
from input import read_int, read_value
from playerfield import PlayerField, check_field

DEFAULT_PUZZLE_FILE = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'example_puzzles', 'puzzle.txt'))
VALID_VALUES = ["x", ".", " "]


def turn(player_field: PlayerField) -> None:
    '''Play a turn'''
    y = read_int(f"Enter row (1-{player_field.height}): ", 1, player_field.height) - 1
    x = read_int(f"Enter column (1-{player_field.width}): ", 1, player_field.width) - 1
    value = read_value("Enter value: ", VALID_VALUES)
    player_field.place(x, y, value)
            

def play_game(player_field: PlayerField, blocks: Blocks) -> None:
    '''Play a nonogram game'''
    while not check_field(player_field, blocks):
        # Clear terminal window
        os.system("cls" if os.name == "nt" else "clear")
        display_game(player_field, blocks)
        turn(player_field)

    print("You win!")
    

def main() -> None:
    # Read puzzle file from arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default=DEFAULT_PUZZLE_FILE, help="Puzzle file")
    args = parser.parse_args()

    blocks = Blocks()
    blocks.create_from_file(args.file)

    num_rows = blocks.get_num_rows()
    num_cols = blocks.get_num_cols()

    player_field = PlayerField(num_cols, num_rows)

    play_game(player_field, blocks)


if __name__ == "__main__":
    main()
