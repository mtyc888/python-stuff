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

class Priviledges:
    def __init__(self, priviledge):
        self.priviledge = priviledge
        
    def show_priviledges(self):
        for priv in self.priviledge:
            print(f"{priv}")
            
class Admin(User):
    def __init__(self, first_name, last_name, age, priviledges):
        super().__init__(first_name, last_name, age)
        self.priviledges = Priviledges(priviledges)


def main():
    admin = Admin('marvin', 'tan', 25, ['a','b','c'])
    admin.priviledges.show_priviledges()
    
main()
            
        
    