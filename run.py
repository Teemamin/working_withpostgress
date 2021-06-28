from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey,
    Integer, String, MetaData
)


# executing the command from our local chinook DB
# /// 3 slashes signifies our DB is hosted locally within our wrkspce enviroment
db = create_engine("postgresql:///chinook")

# the metadata class will contain a  colection of our table objects n associated data within
# those objcts
# recursive data about data
meta = MetaData(db)

# create varible for "Artist" table
artist_table = Table(
    "Artist",meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create varible for "Album" table
album_table = Table(
    "Album",meta,
    Column("AlbumId",Integer,primary_key=True),
    Column("Title",String),
    Column("ArtistId",Integer,ForeignKey("artist_table.ArtistId"))

)
# create varible for "Track" table
track_table = Table(
    "Track",meta,
    Column("TrackId",Integer,primary_key=True),
    Column("Name",String),
    Column("AlbumId",Integer,ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId",Integer,primary_key=False),
    Column("GenreId",Integer,primary_key=False),
    Column("Composer",String),
    Column("Milliseconds",Integer),
    Column("Bytes",Integer),
    Column("UnitPrice",Float)

)

# making the connection
with db.connect() as connection:
    # query 1 select all records from the Artist table
    # select_query = artist_table.select()

    # query 2 select only the Name column from Artist table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # query 3 select only Queen from Artist table
    # select_query = artist_table.select().where(artist_table.c.Name=="Queen")

    # query 4 select only by ArtistId 51 from Artist table
    # select_query = artist_table.select().where(artist_table.c.ArtistId==51)

    # query 5 select only the albums with ArtistId 51 from Album table
    # select_query = album_table.select().where(album_table.c.ArtistId==51)

    # query 6  select all  from the Track table where Composer is Queen
    select_query = track_table.select().where(track_table.c.Composer=="Queen")










    # execute the command above and save it to results vaible
    results = connection.execute(select_query)
    for result in results:
        print(result)