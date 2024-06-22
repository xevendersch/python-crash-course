class User():
    """A simple attempt to model a user."""
    def __init__(self, first_name, last_name, age, gender, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts
    
    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"{self.first_name} {self.last_name} is {self.age} years old and is a {self.gender}.")
    
    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")
    
    def increment_login_attempts(self):
        """Increment the login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0

user1 = User("Ali", "Ahmed", 25, "Male", 0)
user1.describe_user()
user1.greet_user()

user2 = User("Ken", "Tanaka", 21, "Male", 0)
user2.describe_user()
user2.greet_user()

user1.increment_login_attempts()
print(f"The login attempts for user1 is {user1.login_attempts}.")

user1.reset_login_attempts()
print(f"The login attempts for user1 is {user1.login_attempts}.")