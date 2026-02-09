import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll(self):
        randomNum = random.randrange(1,self.sides)
        print(f"{randomNum}")
        
def main():
    die6 = Die()
    print("Rolling 6 sided die, 10 times")
    for i in range(10):
        die6.roll()
    die10 = Die(10)
    print("Rolling 10 sided die, 10 times")
    for i in range(10):
        die10.roll()
    die20 = Die(20)
    print("Rolling 20 sided die, 10 times")
    for i in range(10):
        die20.roll()
        
main()