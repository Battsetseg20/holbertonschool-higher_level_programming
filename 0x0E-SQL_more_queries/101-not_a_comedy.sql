-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
      SELECT tv_shows.title
      FROM tv_genres
      INNER JOIN tv_show_genres
      ON (tv_genres.id = tv_show_genres.genre_id)

      INNER JOIN tv_shows
      ON (tv_show_genres.show_id = tv_shows.id)
      WHERE tv_genres.name = "Comedy")
ORDER BY tv_shows.title ASC;
