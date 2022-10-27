from blocks import Blocks
from playerfield import PlayerField


def get_max_list_length(lists: list[list[int]]) -> int:
    '''Get the max length of a list of lists'''
    return max(len(l) for l in lists)


def display_game(player_field: PlayerField, blocks: Blocks) -> None:
    '''Display the game, works for values 1-99'''
    print("Nonogram")
    row_blocks = blocks.get_row_blocks()
    col_blocks = blocks.get_col_blocks()
    
    max_row_len = get_max_list_length(row_blocks)
    max_col_len = get_max_list_length(col_blocks)

    # Display column blocks
    left_padding = " " * (3 * max_row_len + 1)
    for i in range(max_col_len):
        print(left_padding, end="")
        for col in col_blocks:
            if i < max_col_len - len(col):
                print(" ", end="  ")
            else:
                value = col[i - (max_col_len - len(col))]
                end = "  " if value < 10 else " "
                print(col[i - max_col_len + len(col)], end=end)
        print()

    # Display row blocks and player field
    for y, row in enumerate(player_field.grid):
        for i in range(max_row_len - len(row_blocks[y])):
            print(" ", end="  ")
        for block in row_blocks[y]:
            end = "  " if block < 10 else " "
            print(block, end=end)
        print(" ", end="")
        for value in row:
            print(value, end="  ")
        print()
