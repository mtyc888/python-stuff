class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
    def set_number_served(self, num):
        self.number_served = num
    def increment_number_served(self, num):
        self.number_served += num

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['strawberry', 'chocolate', 'butterscotch', 'vanilla']
    def display_flavours(self):
        for flav in self.flavours:
            print(f"I like {flav}")
    def show_flavours(self):
        print(self.flavours) 
def main():
    ice_cream = IceCreamStand('ice cream stand', 'haha', 'hot')
    ice_cream.display_flavours()
    ice_cream.show_flavours()

main()