# TODO
from cs50 import get_float

while True:
    cents = get_float("Change: ")
    if cents > 0:
        break

cents = round(cents * 100)

count = 0

while cents >= 25:
    cents -= 25
    count += 1

while cents >= 10:
    cents -= 10
    count += 1

while cents >= 5:
    cents -= 5
    count += 1

while cents >= 1:
    cents -= 1
    count += 1

print("Total coins:", count)
