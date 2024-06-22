from random import randint
from random import choice

print(randint(1, 6)) # Menghasilkan angka acak antara 1-6

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players) # Menghasilkan pilihan acak dari list players
print(first_up.title())

