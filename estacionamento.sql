DROP DATABASE IF EXISTS estacionamento;
CREATE DATABASE estacionamento;
CREATE USER estacionamento IDENTIFIED BY "estacione";
DROP USER IF EXISTS estacionamento;
GRANT ALL ON *.* TO estacionamento WITH GRANT OPTION;

SELECT * FROM restaurant.users;

SELECT * FROM estacionamento.users;