import psycopg2


# connect to chinook DB
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the DB
cursor = connection.cursor()
# query 1 select all artist from the artist table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 name  from the artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 select all  from the artist table where name is queen
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s',["Queen"])

# query 4 select all  from the artist table where Id is 51
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s',[51])

# query 5 select all  from the album table where ArtistId is 51
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s',[51])

# query 6 select all  from the Track table where Composer is Queen
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s',["Queen"])






# fetch the results(multiple)
results = cursor.fetchall()

# fetch the result(single)
# result = cursor.fetchone()

# end conncetion to DB
connection.close()
for result in results:
    print(result)