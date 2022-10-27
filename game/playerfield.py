from dataclasses import dataclass

from blocks import Blocks


@dataclass
class PlayerField:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.grid = [[" " for _ in range(width)] for _ in range(height)]

    def place(self, x: int, y: int, value: str) -> None:
        self.grid[y][x] = value


def get_connected_blocks(values: list[str]) -> list[int]:
    '''Get the number of connected blocks in a row or column'''
    blocks = []
    current_block = 0
    for value in values:
        if value == "x":
            current_block += 1
        else:
            if current_block > 0:
                blocks.append(current_block)
            current_block = 0
    if current_block > 0:
        blocks.append(current_block)
    return blocks


def check_field(field: PlayerField, blocks: Blocks) -> bool:
    '''Check if the player field matches the blocks'''
    for y, row in enumerate(field.grid):
        if get_connected_blocks(row) != blocks.get_row_blocks()[y]:
            return False
    for x in range(field.width):
        col = [row[x] for row in field.grid]
        if get_connected_blocks(col) != blocks.get_col_blocks()[x]:
            return False
    return True
