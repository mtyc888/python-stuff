def make_album(artist, title):
    album_dict = {
        'artist':artist.title(),
        'album':title.title()
    }
    return album_dict

while True:
    
    artist = input("Enter artist name, press 1 to quit\n")
    if artist == "1":
        break
    title = input("Enter title, press 1 to quit\n")
    if title == '1':
        break
    
    print(make_album(artist, title))
    
    