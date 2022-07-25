#! /bin/sh
psql -U postgres <<-EOSQL
 CREATE DATABASE git;
EOSQL

psql -U postgres --dbname "git" -f /setup/init.sql