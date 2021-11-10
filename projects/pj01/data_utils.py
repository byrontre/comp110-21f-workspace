"""Functions for Filtering Survey Data."""


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv file into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented able into a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    """Return a Column with N Rows."""
    stem: dict[str, list[str]] = {} 
    for keys in x:
        store: list[str] = []
        i: int = 0
        if len(x[keys]) < y:
            y = len(x[keys])
        while i < y:
            store.append(x[keys][i])
            i += 1
        stem[keys] = store 
    return stem


def select(a: dict[str, list[str]], b: list[str]) -> dict[str, list[str]]:
    """Produce Subset of Columns from Total Column Data."""
    totem: dict[str, list[str]] = {} 
    for keys in b:
        totem[keys] = a[keys]
    return totem


def count(intro: list[str]) -> dict[str, int]:
    """Return the Dict of Frequencies."""
    outro: dict[str, int] = {}
    i: int = 0
    while i < len(intro):
        if intro[i] in outro:
            outro[intro[i]] += 1
        else:
            outro[intro[i]] = 1
        i += 1
    return outro


def rosebud(root: dict[str, list[str]]) -> list[str]:
    """Tally Values from Interesting and Difficulty Columns."""
    i: int = 0
    poppy: list[str] = []
    for keys in root:
        while i < len(root[keys]):
            if int(root[keys][i]) >= 5:
                poppy.append(root[keys][i])
            i += 1
    return poppy


def periwinkle(root: dict[str, list[str]]) -> list[str]:
    """Tally Values from Office Hour Visit Column."""
    violet: list[str] = []
    i: int = 0
    for keys in root:
        while i < len(root[keys]):
            if int(root[keys][i]) <= 3:
                violet.append(root[keys][i])
            i += 1
    return violet
