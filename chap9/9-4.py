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

def main():
    res = Restaurant('restaurant ching', 'chinese food')
    res.open_restaurant()
    res.describe_restaurant()
    
    print(f"{res.restaurant_name} served {res.number_served} customers")
    res.set_number_served(50)
    print(f"{res.restaurant_name} served {res.number_served} customers")
    print("incrementing by 50")
    res.increment_number_served(50)
    print(f"{res.restaurant_name} served {res.number_served} customers")

main()