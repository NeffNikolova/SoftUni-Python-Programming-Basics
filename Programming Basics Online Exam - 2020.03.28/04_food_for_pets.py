days = int(input())
all_food = int(input())

total_biscuits = 0
p_eaten = 0
p_dog = 0
p_cat = 0

for i in range(1, days + 1):
    dog_ate = float(input())
    cat_ate = float(input())
    p_dog += dog_ate
    p_cat += cat_ate
    p_eaten += (dog_ate + cat_ate)

    if i % 3 == 0:
        total_biscuits += (dog_ate + cat_ate) * 0.10

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{(p_eaten / all_food * 100):.2f}% of the food has been eaten.")
print(f"{(p_dog / p_eaten * 100):.2f}% eaten from the dog.")
print(f"{(p_cat / p_eaten * 100):.2f}% eaten from the cat.")


