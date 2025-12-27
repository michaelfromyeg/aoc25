from pathlib import Path


def read_input(debug: bool = False) -> list[str]:
    import inspect

    caller_file = Path(inspect.stack()[1].filename)
    input_file = caller_file.parent / ("test.txt" if debug else "input.txt")
    with open(input_file, encoding="utf-8") as f:
        return f.readlines()
