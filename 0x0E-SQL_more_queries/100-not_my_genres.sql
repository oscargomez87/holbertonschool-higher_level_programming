-- List all genres not linked to the show Dexter
SELECT
	tv_genres.name
FROM
	tv_genres
LEFT OUTER JOIN tv_show_genres
     ON tv_genres.id = tv_show_genres.genre_id
     AND tv_show_genres.show_id = (
     	 SELECT
		tv_shows.id
	 FROM
		tv_shows
	 WHERE title = 'Dexter')
WHERE show_id IS NULL
ORDER BY tv_genres.name ASC;
