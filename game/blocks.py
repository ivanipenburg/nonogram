from dataclasses import dataclass


@dataclass
class Blocks:
    def create_from_file(self, filename: str) -> None:
        with open(filename) as f:
            row = f.readline()
            column = f.readline()

        self.row_blocks = [[int(x) for x in col.split(",")] for col in row.split("/")]
        self.col_blocks = [[int(x) for x in col.split(",")] for col in column.split("/")]

    def get_num_rows(self) -> int:
        return len(self.row_blocks)

    def get_num_cols(self) -> int:
        return len(self.col_blocks)

    def get_row_blocks(self) -> list[list[int]]:
        return self.row_blocks

    def get_col_blocks(self) -> list[list[int]]:
        return self.col_blocks
