from random import choice

numbers = list(range(1, 11))
print(numbers)

letters = ['a', 'k', 'm', 'g', 'y']
print(letters)

choose_number = choice(numbers)
choose_letter = choice(letters).upper()

win = f"{choose_number}{choose_letter}"
print(f"Any ticket matching '{win}' wins!")

