SELECT Track.Name AS nome_musica , Genre.name AS nome_genero FROM Track

JOIN Genre ON Genre.GenreId = Track.TrackId 