"""Practice with dictionaries."""

__author__ = "730345086"


def invert(trace: dict[str, str]) -> dict[str, str]:
    """Flip the Dictionary."""
    filler: dict[str, str] = {}
    for keys in trace:
        if keys in filler:
            raise KeyError("Access denied: Duplicate keys detected.")
        else:
            filler[trace[keys]] = keys
    return filler
            

def favorite_color(red: dict[str, str]) -> str:
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
            this_color = keys
        counter = score[keys]
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