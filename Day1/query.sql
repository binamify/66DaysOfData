SELECT * FROM movies_data
-- returns whole table

SELECT COUNT(*) FROM movies_data
-- returns number of data(rows)

SELECT Actors FROM movies_data
-- returns the rows of actor from dataset

SELECT DirectorName FROM movies_data WHERE year > 2010
-- returns the name of director from movies whch are after 2010

SELECT DirectorName,ProducerName FROM movies_data WHERE year = 2012
-- returns multiple rows

SELECT MovieName FROM movies_data WHERE DirectorName = 'Sambhu Thapa' AND year <2005
--returns result based on multiple condition and conditions can be as many

SELECT MovieName FROM movies_data WHERE year BETWEEN 2000 AND 2010
-- returns movies list between 2000 and 2010


--AND and OR can be combined in many ways
SELECT MovieName FROM movies_data WHERE year = 2010 OR year = 2012 AND(DirectorName = 'Ram Rai' OR DirectorName = 'Sovit Basnet')
-- Returns movie list either of year 2010 or 2012 which may be directed by any

SELECT MovieName FROM movies_data WHERE ProducerName IS NULL
-- returns movies list whose producer name is not listed

SELECT MovieName FROM movies_data WHERE ProducerName IS NOT NULL
-- returns movies list whose producer name  not listed


--LIKE and NOT LIKE works on  search pattern using wild card

SELECT MovieName FROM movies_data WHERE MovieName LIKE 'A%'
-- returns list of movies whose name start with a

SELECT MovieName FROM movies_data WHERE MovieName LIKE '_a%'
-- returns list of movies whose second letter is a

SELECT MovieName FROM movies_data WHERE MovieName LIKE 'm_ya'
-- possible pattern can be maya, moya, meya -searches that