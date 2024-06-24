#Define a class called Song, it will show the lyrics of a song.
#Its __init__() method should have two arguments: self and lyrics (a list).
#Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

class Song ():
    def __init__(self,lyrics):
        self.lyrics = lyrics
        
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


Spaces = Song([
    "Spaces between us",
    "Keeps getting deeper",
    "Harder to reach you even though I try..."
])

Spaces.sing_me_a_song()