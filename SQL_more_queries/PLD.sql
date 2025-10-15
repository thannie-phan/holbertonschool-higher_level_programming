USE hbtn_0d_tvshows;

SELECT genre_id, COUNT(*) AS count_occurrences
FROM tv_show_genres
GROUP BY genre_id
HAVING COUNT(*) > 1;

