-- Select all genres and the number of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY COUNT(tv_show_genres.show_id) DESC;
