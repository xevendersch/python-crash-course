class Restaurant():
    """A simple class for restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is restaurant {self.restaurant_name}.")
        print(f"Our speciality is {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"Restaurant is open!")

class IceCreamStand(Restaurant):
    """A simple class for ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavors(self):
        print(f"We have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Honolu", "Ramen", 'Vanilla')
ice_cream_stand.display_flavors()

