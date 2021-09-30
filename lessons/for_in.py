"""An Example of For-In Syntax."""

names: list[str] = ["Byron", "Lauren", "Jason", "Hannah"]

print("While output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for..in output:")
for name in names:
    print(name)