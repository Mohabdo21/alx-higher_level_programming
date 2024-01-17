-- list all genres not linked to the show Dexter
SELECT name 
FROM tv_genres 
WHERE id NOT IN (
    SELECT genre_id 
    FROM tv_show_genres 
    WHERE show_id = (
        SELECT id 
        FROM tv_shows 
        WHERE title = 'Dexter'
    )
)
ORDER BY name;
