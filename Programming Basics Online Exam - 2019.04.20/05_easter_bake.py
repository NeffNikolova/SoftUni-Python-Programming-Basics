import math

nr_breads = int(input())

all_sugar = 0
all_flour = 0
max_flour = 0
max_sugar = 0

for _ in range(nr_breads):
    current_sugar = int(input())
    current_flour = int(input())

    all_sugar += current_sugar
    all_flour += current_flour

    if current_sugar > max_sugar:
        max_sugar = current_sugar

    if current_flour > max_flour:
        max_flour = current_flour

needed_sugar_p = math.ceil(all_sugar / 950)
needed_flour_p = math.ceil(all_flour / 750)

print(f"Sugar: {needed_sugar_p}")
print(f"Flour: {needed_flour_p}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
