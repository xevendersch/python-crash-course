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

restaurantA = Restaurant("Honolu", "Ramen")
restaurantB = Restaurant("Kaalash", "Indian")
restaurantC = Restaurant("Albaik", "Arabian")

restaurantA.describe_restaurant()
restaurantA.open_restaurant()

restaurantB.describe_restaurant()
restaurantB.open_restaurant()

restaurantC.describe_restaurant()
restaurantC.open_restaurant()
