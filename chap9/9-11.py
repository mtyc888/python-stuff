import User as u
from User import Priviledges


def main():
    admin = u.Admin('marvin', 'tan', 25, ['a','b','c'])
    admin.priviledges.show_priviledges()
    
main()
            
        
    