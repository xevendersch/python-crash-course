class User():
    """A simple attempt to model a user."""
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"{self.first_name} {self.last_name} is {self.age} years old and is a {self.gender}.")
    
    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")

user1 = User("Ali", "Ahmed", 25, "Male")
user1.describe_user()
user1.greet_user()

user2 = User("Ken", "Tanaka", 21, "Male")
user2.describe_user()
user2.greet_user()