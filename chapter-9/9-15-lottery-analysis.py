from random import choice

numbers = list(range(1, 11))
letters = ['a', 'k', 'm', 'g', 'y']

my_ticket = "2Y"  # Contoh tiket yang ingin kita menangkan
attempts = 0
lottery_price = 100

while True:
    choose_number = choice(numbers)
    choose_letter = choice(letters).upper()
    combined = f"{choose_number}{choose_letter}"
    attempts += 1
    if combined == my_ticket:
        print(f"Anda menang dengan tiket {my_ticket} setelah {attempts} percobaan!")
        break

uang = lottery_price * attempts
print(f"Anda perlu memiliki uang sebesar JPY{uang} untuk memenangkan lottery")

