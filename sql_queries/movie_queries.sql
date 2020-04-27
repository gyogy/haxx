
### First queries

SELECT address
  FROM STUDIO
  WHERE STUDIO.NAME = "MGM"

SELECT birthdate
  FROM MOVIESTAR
  WHERE MOVIESTAR.NAME = "Kim Basinger"

SELECT name
  FROM MOVIEEXEC
  WHERE MOVIEEXEC.networth > 10000000

SELECT name
  FROM MOVIESTAR
  WHERE MOVIESTAR.gender = "M" OR MOVIESTAR.address = "Prefect Rd."

INSERT INTO MOVIESTAR
  VALUES ("Bahari Zaharov", "Kofa No.5", "M", '1980-08-12')

DELETE from STUDIO
  WHERE Address LIKE '%5%'

UPDATE MOVIE
  SET Studioname = 'Fox'
  WHERE title LIKE '%star%'


### Relations

SELECT starname
  FROM STARSIN
  JOIN MOVIESTAR ON STARSIN.starname = MOVIESTAR.name
  WHERE STARSIN.movietitle = 'Terms of Endearment' AND MOVIESTAR.gender = 'M'

SELECT Starname
  FROM STARSIN
  JOIN MOVIE ON MOVIE.title = STARSIN.movietitle
  JOIN STUDIO ON STUDIO.name = MOVIE.STUDIONAME
  WHERE STARSIN.movieyear = 1995 AND MOvie.studioname = 'MGM'



ALTER TABLE STUDIO
  ADD COLUMN President_CERT INTEGER REFERENCES MOVIEEXEC(CERT);

UPDATE STUDIO
  SET President_cert = 123
  WHERE name = 'MGM'

SELECT MOVIEEXEC.Name
  FROM MOVIEEXEC
  JOIN STUDIO ON STUdio.president_cert = MOVIEEXEC.cert
  WHERE studio.name = 'MGM'
