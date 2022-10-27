def read_int(prompt: str, min_value: int, max_value: int) -> int:
    '''Read an integer between a min and max value'''
    while True:
        line = input(prompt)
        try:
            value = int(line)
            if value < min_value or value > max_value:
                print(f"Please enter a value between {min_value} and {max_value}")
            else:
                return value
        except ValueError:
            print("Please enter a number")


def read_value(prompt: str, valid_values: list[str]) -> str:
    '''Read a value from a list of valid values'''
    while True:
        line = input(prompt)
        if line not in valid_values:
            valid_values_str = ' '.join(f"'{v}'" for v in valid_values)
            print(f"Please enter one of {valid_values_str}")
        else:
            return line
