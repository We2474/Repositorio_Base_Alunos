SELECT name ,Composer,UnitPrice FROM Track

JOIN album ON Album.AlbumId = Track.TrackId 

WHERE Composer = 'AC/DC'
