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

class Admin(User):
    """A simple attempt to model an admin."""
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()

class Privileges():
    """A simple attempt to model privileges."""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        """Display the admin's privileges."""
        print(f"Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin("Ali", "Ahmed", 25, "Male")
admin.privileges.show_privileges()

