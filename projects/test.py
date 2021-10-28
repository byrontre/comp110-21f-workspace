"""This is the Testing Arena for Things to See How They Run."""

from random import randint 

safe: dict[int, str] = {2: "No", 4: "One", 6: "Is", 8: "As", 10: "Lucky", 12: "As", 14: "Us"}
lock_box: dict[str, int] = {}
print("We need a resolution.")
for keys in safe:
    lock_box[safe[keys]] = randint(1, 10)
    if safe[keys] in lock_box:
        lock_box[safe[keys]] += randint(1, 10)
for keys in lock_box:
    i: int = lock_box[keys]
    if i <= 5:
        lock_box.pop(keys)
    else:
        if i <= 10:
            lock_box[keys] += randint(1, 10)

print(lock_box)