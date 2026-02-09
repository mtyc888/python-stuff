from Admin import Admin
from Priviledges import Priviledges


def main():
    admin = Admin('marvin', 'tan', 25, ['a','b','c'])
    admin.priviledges.show_priviledges()
    
main()
            
        
    