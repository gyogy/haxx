SELECT SHIPS.NAME, CLASSES.COUNTRY, CLASSES.NUMGUNS, SHIPS.LAUNCHED  
          FROM SHIPS 
          JOIN CLASSES ON CLASSES.CLASS = SHIPS.CLASS;

# Im confused by the second querys description.
# The below query gives me the only class w/o a ship to its name, i.e. the Bismark class:

# SELECT CLASSES.CLASS 
#          FROM `CLASSES` 
#          LEFT OUTER JOIN SHIPS ON SHIPS.CLASS = CLASSES.CLASS 
#          WHERE SHIPS.NAME IS NULL;

# But its not clear to me how I should combine the result with the top query.

SELECT SHIP 
          FROM OUTCOMES 
          JOIN BATTLES ON BATTLES.NAME = OUTCOMES.BATTLE 
          WHERE BATTLES.DATE >= '1942-1-1' AND BATTLES.DATE < '1943-1-1';

SELECT CLASSES.COUNTRY, NAME FROM SHIPS 
          LEFT OUTER JOIN OUTCOMES ON SHIPS.NAME = OUTCOMES.SHIP 
          JOIN CLASSES ON SHIPS.CLASS = CLASSES.CLASS 
          WHERE OUTCOMES.RESULT IS NULL;

