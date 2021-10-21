"""This is the Testing Arena for Things to See How They Run."""


case_bot: dict[int, str] = {}

snatch: str = '\U0001F430'
catch: str = '\U0001F419'
latch: str = '\U0001F436'

case_bot[10] = snatch
case_bot[12] = catch
case_bot[14] = latch

print(case_bot)

case_bot.pop(12)

filler: str = '\U0001F456'

case_bot[16] = filler

print(case_bot)

safe_bot: dict[str, int] = {}

for keys in case_bot:
    safe_bot[case_bot[keys]] = keys

print(safe_bot)