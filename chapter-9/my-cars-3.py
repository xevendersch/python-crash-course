from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('Volkswagen', 'Beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('Tesla', 'Model S', 2021)
print(my_tesla.get_descriptive_name())