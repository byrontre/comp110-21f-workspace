"""Utility functions."""

__author__ = "730345086"

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
    return stem


def select(a: dict[str, list[str]], b: list[str]) -> dict[str, list[str]]:
    """Produce Subset of Columns from Total Colum Data."""
    reject: dict[str, list[str]] = {}
    return reject 


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine Two Dicts into One Dict."""
    combo: dict[str, list[str]] = {}
    return combo
