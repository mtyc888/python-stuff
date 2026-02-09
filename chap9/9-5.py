class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.age}")
    
    def greet_user(self):
        print(f"hello {self.first_name} {self.last_name}")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    

def main():
    user1 = User("rock", "roll", "25")
    user1.describe_user()
    user1.greet_user()
    
    print(f"login attempts: {user1.login_attempts}")
    
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    
    print(f"login attempts: {user1.login_attempts}")
    
    user1.reset_login_attempts()
    
    print(f"login attempts: {user1.login_attempts}")
    
main()
    