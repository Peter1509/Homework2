from smartninja_sql.sqlite import SQLiteDatabase
db = SQLiteDatabase("Chinook_Sqlite.sqlite")

#What order (Invoice) was the most expensive? Which one was the cheapest?
db.pretty_print("""SELECT Invoice.InvoiceId, Invoice.InvoiceDate, Invoice.CustomerId, MAX(Invoice.Total)
            FROM Invoice;""")

db.pretty_print("""SELECT Invoice.InvoiceId, Invoice.InvoiceDate, Invoice.CustomerId, MIN(Invoice.Total)
            FROM Invoice;""")

#Which city (BillingCity) has the most orders?
db.pretty_print("""SELECT Invoice.BillingCity, COUNT(*) AS CountOrders
            FROM Invoice
            GROUP BY Invoice.BillingCity
            ORDER BY CountOrders DESC;""")

#Calculate (or count) how many tracks have this MediaType: Protected AAC audio file.
db.pretty_print("""SELECT MediaType.Name, COUNT(Track.MediaTypeId)
                FROM Track
                INNER JOIN MediaType ON MediaType.MediaTypeId=Track.MediaTypeId
                WHERE MediaType.Name='Protected AAC audio file';""")

#Find out what Artist has the most albums? (hint: check ORDER BY)
db.pretty_print("""SELECT Artist.Name, COUNT(*) AS CountAlbum
                FROM Artist
                INNER JOIN Album ON Artist.ArtistId = Album.ArtistId
                GROUP BY Album.ArtistId
                ORDER BY CountAlbum DESC;""")

#What genre has the most tracks?
db.pretty_print("""SELECT Genre.Name, COUNT(Track.GenreId) AS CountGenre
                FROM Genre
                INNER JOIN Track ON Genre.GenreId = Track.GenreId
                GROUP BY Track.GenreId
                ORDER BY CountGenre DESC;""")

#Which customer spent the most money so far?
db.pretty_print("""SELECT Customer.CustomerId, Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS CustomerSum
                FROM Invoice
                INNER JOIN Customer ON Invoice.CustomerId = Customer.CustomerId
                GROUP BY Invoice.CustomerId
                ORDER BY CustomerSum DESC;""")

#What songs were bought with each order? (hint: here you have to do a many-to-many 
# SQL query with three tables: Track, Invoice and InvoiceLine. You have to do two JOINS here)
db.pretty_print("""SELECT Invoice.InvoiceId, Track.Name
                FROM InvoiceLine
                FULL JOIN Invoice ON Invoice.InvoiceId = InvoiceLine.InvoiceId
                FULL JOIN Track ON Track.TrackId = InvoiceLine.TrackId
                ;""")
#-> Ich bekomem die Meldung, dass FULL JOINS nicht unterstützt werden. 
#Bin mir aber sowieso nicht sicher, ob man das so schreiben kann. 
#Gerne im Kurs besprechen! 