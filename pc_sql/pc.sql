SELECT AVG(speed) FROM PC

SELECT product.maker, AVG(laptop.screen)
  FROM laptop 
  JOIN product ON laptop.model = product.model
  GROUP BY product.maker

SELECT AVG(speed) FROM laptop WHERE price > 1000

SELECT hd, AVG(price) FROM pc GROUP BY hd

SELECT speed, AVG(price)
  FROM pc
  GROUP BY speed
  HAVING speed > 500

SELECT AVG(pc.price)
  FROM pc
  JOIN product
  ON pc.model = product.model
  WHERE product.maker = 'A'

SELECT AVG(price) FROM
  (SELECT pc.price  
  FROM product 
  LEFT OUTER JOIN pc ON pc.model = product.model 
  WHERE maker = 'B' 
  UNION 
  SELECT laptop.price 
  FROM product 
  LEFT OUTER JOIN laptop ON laptop.model = product.model 
  WHERE maker = 'B');

SELECT maker, COUNT(model)
  FROM product
  GROUP BY maker
  HAVING COUNT(model)>3;

SELECT product.maker, MAX(pc.price) 
  FROM pc 
  JOIN product ON pc.model = product.model;

SELECT maker, AVG(pc.hd) FROM product 
  LEFT OUTER JOIN pc ON pc.model = product.model 
  GROUP BY maker  
  HAVING maker IN (SELECT DISTINCT maker FROM product WHERE type = 'Printer') 
  AND maker IN (SELECT DISTINCT maker FROM product WHERE type ='PC');

