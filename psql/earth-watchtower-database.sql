-- Create earth-watchtower database

DROP DATABASE IF EXISTS "earth-watchtower" WITH (FORCE);
CREATE DATABASE "earth-watchtower"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
