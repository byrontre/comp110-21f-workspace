"""Practice with dictionaries."""

__author__ = "730345086"


def invert(trace: dict[str, str]) -> dict[str, str]:
    """Flip the Dictionary."""
    filler: dict[str, str] = {}
    for keys in trace:
        filler[trace[keys]] = keys
        if keys in filler:
            raise KeyError("Access denied: Duplicate keys detected.")
    return filler
            

def favorite_colors(red: dict[str, str]) -> str:
    """Pick a Color, Return the Most Frequent."""
    score: dict[str, int] = {}
    this_color: str = ""
    counter: int = 0
    for keys in red:
        score[red[keys]] = 1
        if red[keys] in score:
            score[red[keys]] += 1
    for keys in score:
        if score[keys] > counter:
            counter = score[keys]
            this_color = keys
    return this_color
        

def count(value: list[str]) -> dict[str, int]:
    """If It's There, Add One... if Not, Move On."""
    new_list: dict[str, int] = dict()
    i: int = 0
    while i < len(value):
        if value[i] in new_list:
            new_list[value[i]] += 1
        else: 
            new_list[value[i]] = 1
        i += 1
    return new_list

    