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
