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

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.priviledges = ['can add post', 'can delete post', 'can ban post']
    def show_priviledges(self):
        for priv in self.priviledges:
            print(f"{priv}")

def main():
    admin = Admin('marvin', 'tan', 25)
    admin.show_priviledges()
    
main()
            
        
    