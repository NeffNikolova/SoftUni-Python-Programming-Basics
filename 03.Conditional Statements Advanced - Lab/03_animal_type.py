animal = input()

animal_class = None

if animal.lower() == 'dog':
    animal_class = 'mammal'
elif animal.lower() == 'crocodile' or animal.lower() == 'tortoise' or animal.lower() == 'snake':
    animal_class = 'reptile'
else:
    animal_class = 'unknown'
print(animal_class)