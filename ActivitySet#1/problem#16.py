# Databases
# https://www.py4e.com/lessons/database
CREATE TABLE ar( 
  name VARCHAR(128), 
  age INTEGER
);
DELETE FROM ar ;
INSERT INTO ar (name, age) VALUES ('Beatriz', 26);
INSERT INTO ar (name, age) VALUES ('Kainui', 31);
INSERT INTO ar(name, age) VALUES ('Janel', 22);
INSERT INTO ar (name, age) VALUES ('Sarabeth', 30);
SELECT hex(name || age) AS X FROM ar ORDER BY X