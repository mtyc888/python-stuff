from User import User
from Priviledges import Priviledges 
class Admin(User):
    def __init__(self, first_name, last_name, age, priviledges):
        super().__init__(first_name, last_name, age)
        self.priviledges = Priviledges(priviledges)