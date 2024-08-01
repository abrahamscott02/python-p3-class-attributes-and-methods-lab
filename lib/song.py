class Song:
    count = 0 # Class Attribute keeps track of total number of songs created
    genres = [] # Class Attribute is a list that will store unique genres of songs
    artists = [] # Class Attribute is a list that will store unique artists of songs
    genre_count = {} # Class Attribute is a dictionary that will store the count of songs for each genre
    artist_count = {} # Class Attribute is a dictionary that will store the count of songs for each artist

    # Instance Attributes
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Class method calls
        Song.add_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
