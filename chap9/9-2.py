class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

def main():
    res = Restaurant('restaurant ching', 'chinese food')
    res.open_restaurant()
    res.describe_restaurant()

    res1 = Restaurant('restaurant ching1', 'mexican food')
    res1.open_restaurant()
    res1.describe_restaurant()
    
    res2 = Restaurant('restaurant ching2', 'steakhouse')
    res2.open_restaurant()
    res2.describe_restaurant()
main()