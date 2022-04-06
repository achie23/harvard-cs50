-- How to connect to a database
-- Enter psql -U userName databaseName e.g.
psql -U abrian lecture3
-- Enter password: 
2326
-- Creating database
CREATE USER userName WITH PASSWORD 'mypassword';
CREATE DATABASE databaseName WITH userName ENCODING 'UTF8' LC_COLLATE='English_United States' LC_CTYPE='English_United States';
-- Basic commands
\c databaseName
\l or \l+ -- to list database
\d -- list of relations
\q -- to log out
