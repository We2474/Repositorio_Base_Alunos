SELECT Album.Title AS nomeDoAlbum, Artist.Name AS NomeDoArtistaOuBanda
FROM Album

JOIN Artist ON Album.ArtistId = Artist.ArtistId