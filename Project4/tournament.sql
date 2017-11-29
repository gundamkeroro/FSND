-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- DROP VIEW FIRSR BECAUE IT IS RELY ON TABLE, OR WE CAN NOT DROP TABLE
DROP VIEW IF EXISTS standings;
DROP VIEW IF EXISTS win_view;
DROP VIEW IF EXISTS lose_view;

-- FOR THE SMAE REASON, DROP MATCHES BEFORE DROP NAMES
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS names;

CREATE TABLE names(
	name text,
	id serial,
	primary key (id)
); 

CREATE TABLE matches(
	win serial references names (id),
	lose serial references names (id),
	matchid serial,
	primary key (matchid)
);

CREATE VIEW win_view AS 
SELECT names.id AS id, COUNT(win) AS wins 
FROM names LEFT JOIN matches
ON names.id = matches.win
GROUP BY names.id
ORDER BY wins DESC;

CREATE VIEW lose_view AS 
SELECT names.id AS id, COUNT(lose) AS loses
FROM names LEFT JOIN matches
ON names.id = matches.lose
GROUP BY names.id
ORDER BY loses DESC;

CREATE VIEW standings AS 
SELECT win_view.id AS id, 
name, 
win_view.wins AS wins, 
win_view.wins + lose_view.loses AS matches
FROM names, win_view, lose_view
WHERE names.id = win_view.id AND names.id = lose_view.id
ORDER BY wins DESC;