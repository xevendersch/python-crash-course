class Restaurant():
    """A simple class for restaurant"""

    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"This is restaurant {self.restaurant_name}.")
        print(f"Our speciality is {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"Restaurant is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment

restaurantA = Restaurant("Honolu", "Ramen", 5)

print(f"The restaurant name is {restaurantA.restaurant_name}")
print(f"This restaurant served: {restaurantA.cuisine_type}")

restaurantA.describe_restaurant()
restaurantA.open_restaurant()
restaurantA.set_number_served(10)
restaurantA.increment_number_served(5)
print(f"The restaurant has served {restaurantA.number_served} customers.")
