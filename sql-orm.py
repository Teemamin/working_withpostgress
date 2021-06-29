from sqlalchemy import (
    create_engine, Column, Float, ForeignKey,
    Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# execting instructions from the chinook DB
db = create_engine("postgresql:///chinook")

# base class will grab the meta data that is produced by our DB table schema
# and create a subclass  to map everything back to us within the base variable
base = declarative_base()

# make sure to add the model after the base is created but before the session
# create a class based model for Artist table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class based model for Album table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer,primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer,ForeignKey("Artist.ArtistId"))



# create a class based model for Track table

class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float) 

# instead of connecting to the DB directly,we will ask for a session
# create a new instance of sessionmaker and point it to our engine (the DB)
Session = sessionmaker(db)

# open an actual session by calling the session() sub class defined above
session = Session()

# creating the database using declarative_base sub class
base.metadata.create_all(db)

# query 1 select all records from the Artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=' | ')


# query 2 select only the Name column from Artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# query 3 select only Queen from Artist table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=' | ')

# query 4 select only by ArtistId 51 from Artist table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=' | ')

# query 5 select only the albums with ArtistId 51 from Album table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, sep=' | ')

# query 6  select all  from the Track table where Composer is Queen
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId,
     track.Composer, track.UnitPrice, sep=' | ')




