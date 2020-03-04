-- Could use Join
-- Work
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
     SELECT tv_genres.id, tv_genres.name
     FROM tv_genres
     JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
     JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
     WHERE tv_shows.title="Dexter"
     ORDER BY tv_genres.name ASC
) AS gen_dex
ON tv_genres.id=gen_dex.id
WHERE gen_dex.id IS NULL
ORDER BY tv_genres.name;
© 2020 GitHub, Inc.
