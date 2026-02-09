class Priviledges:
    def __init__(self, priviledge):
        self.priviledge = priviledge
        
    def show_priviledges(self):
        for priv in self.priviledge:
            print(f"{priv}")