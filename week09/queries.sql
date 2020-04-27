CREATE TABLE Languages (
  id INTEGER PRIMARY KEY,
  language VARCHAR(30),
  answer VARCHAR(30),
  answered BOOLEAN,
  guide TEXT);

INSERT INTO languages
  VAlUES (1, "Python", "google", 0, "A folder named Python was created. Go there and fight with program.py!");

INSERT INTO languages
  VAlUES (2, 	"Go", "200 OK", 0, "A folder named Go was created. Go there and try to make Google Go run.");

...  # Repeat query for remaining rows 

ALTER TABLE languages
  ADD Rating INTEGER
  CHECK (Rating BETWEEN 0 AND 9)

UPDATE languages
	SET Rating = 9
    WHERE id = 1

UPDATE languages
	SET Rating = 8
    WHERE id = 2

...  # Repeat query for remaining rows 

UPDATE languages
	SET answered = 1
    WHERE language = "Python" OR language = "Go"

SELECT *
	FROM languages
    WHERE answer = "200 OK" OR answer = "Lambda"

