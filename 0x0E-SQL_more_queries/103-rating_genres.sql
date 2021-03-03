-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
SELECT g.name, sum(c.rate) AS rating
FROM tv_genres g
INNER JOIN tv_show_genres b ON g.id = b.genre_id
INNER JOIN tv_show_ratings c ON b.show_id = c.show_id
GROUP BY g.name
ORDER BY rating DESC;
